from django import forms
from django.forms import ClearableFileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Upload


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['uploaded_file']
        widgets = {
            'uploaded_file': ClearableFileInput(attrs={'multiple': True}),
        }
