from datetime import date
from django.conf import settings
from django.db import models


# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    today = date.today()
    return '{0}/{2}/{1}'.format(instance.user.username, filename, today.strftime("%Y/%m/%d/"))


class Upload(models.Model):
    uploaded_file = models.FileField(null=True, blank=True, upload_to=user_directory_path)
    file_name = models.CharField(max_length=255, null=True)
    date_uploaded = models.DateField(auto_now_add=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.uploaded_file.name
