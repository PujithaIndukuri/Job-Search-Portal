# Generated by Django 3.0.4 on 2020-03-31 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearchapp', '0002_auto_20200330_2053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='company',
            new_name='Company',
        ),
    ]