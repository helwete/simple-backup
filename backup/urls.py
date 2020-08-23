from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  path('', views.index, name='index'),
                  path('settings/', views.settings, name='settings'),
                  path('upload/', views.upload, name='upload'),
                  path('files/', views.files, name='files'),
                  path('file_browser/', views.file_browser, name='file_browser'),
                  path('register/', views.register_page, name="register"),
                  path('login/', views.login_page, name="login"),
                  path('logout/', views.logout_user, name="logout"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
