# Generated by Django 4.2.3 on 2023-08-04 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0004_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_pic',
            field=models.FileField(default='', max_length=200, upload_to='collegeapp/employee_pic'),
        ),
    ]
