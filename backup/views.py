from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


# Create your views here.
from .forms import CreateUserForm, UploadFileForm
from .models import Upload


def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'registration/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'registration/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def index(request):
    return render(request, 'backup/index.html')


@login_required(login_url='login')
def settings(request):
    return render(request, 'backup/settings.html')


@login_required(login_url='login')
def file_browser(request):
    user_name = request.user
    print(user_name)
    return redirect('/media/' + str(user_name))


@login_required(login_url='login')
def files(request):
    date_selected = ""
    all_files = Upload.objects.filter(user=request.user).order_by('-date_uploaded')
    all_dates = Upload.objects.filter(user=request.user).order_by('-date_uploaded').values_list(
        'date_uploaded', flat=True).distinct()

    if request.method == 'POST':
        selection = request.POST.get('dates')
        selection_datetime_obj = datetime.strptime(selection, '%b. %d, %Y')
        if selection:
            date_selected = Upload.objects.filter(user=request.user).filter(
                date_uploaded=selection_datetime_obj.strftime('%Y-%m-%d'))

    context = {
        'all_files': all_files,
        'all_dates': all_dates,
        'date_selected': date_selected
    }

    return render(request, 'backup/files.html', context)


@login_required(login_url='login')
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES, initial={'user': request.user})
        files_to_upload = request.FILES.getlist('uploaded_file')
        if form.is_valid():
            # file is saved
            for file in files_to_upload:
                existing_file = Upload.objects.filter(file_name__exact=file)
                # If no existing file that contains f we can upload it
                if len(existing_file) == 0:
                    file_instance = Upload(uploaded_file=file, user=request.user, file_name=file)
                    file_instance.save()
            return HttpResponseRedirect('/upload')
    else:
        form = UploadFileForm()
    return render(request, 'backup/upload.html', {'form': form})
