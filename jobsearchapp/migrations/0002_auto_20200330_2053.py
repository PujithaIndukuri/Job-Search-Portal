# Generated by Django 3.0.4 on 2020-03-31 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearchapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='Job_Date',
            new_name='Date',
        ),
    ]