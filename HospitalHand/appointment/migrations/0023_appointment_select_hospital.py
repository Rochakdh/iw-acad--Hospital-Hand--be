# Generated by Django 3.1 on 2020-09-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0022_auto_20200901_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='select_hospital',
            field=models.CharField(default=None, max_length=200),
        ),
    ]