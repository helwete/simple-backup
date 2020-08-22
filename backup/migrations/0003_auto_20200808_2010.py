# Generated by Django 3.0.8 on 2020-08-08 20:10

import backup.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backup', '0002_remove_upload_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='upload',
            name='uploaded_file',
            field=models.FileField(blank=True, null=True, upload_to=backup.models.user_directory_path),
        ),
    ]