# Generated by Django 3.1 on 2020-08-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_remove_hospital_doctors'),
        ('categories', '0013_auto_20200818_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ManyToManyField(to='hospital.Hospital'),
        ),
    ]