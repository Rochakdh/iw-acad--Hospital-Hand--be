# Generated by Django 3.1 on 2020-09-12 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0003_notice_model_hospital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice_model',
            name='hospital',
        ),
    ]