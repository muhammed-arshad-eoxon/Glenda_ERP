# Generated by Django 4.1.2 on 2024-10-22 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0003_alter_department_dept_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/'),
        ),
    ]
