# Generated by Django 3.2.5 on 2021-07-12 01:25

from django.db import migrations, models
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20210712_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default-avatar.png', null=True, upload_to=userprofile.models.get_file_path),
        ),
    ]