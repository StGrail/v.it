# Generated by Django 3.1.4 on 2021-01-15 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210115_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancies',
            name='skills',
        ),
    ]
