# Generated by Django 3.1 on 2020-09-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0021_auto_20200901_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient_name',
            field=models.CharField(max_length=200),
        ),
    ]