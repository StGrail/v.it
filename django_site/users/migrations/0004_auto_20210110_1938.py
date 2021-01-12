# Generated by Django 3.1.4 on 2021-01-10 16:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210109_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancies',
            old_name='vacancy_id',
            new_name='id_vacancy',
        ),
        migrations.RemoveField(
            model_name='vacancies',
            name='user',
        ),
        migrations.AddField(
            model_name='vacancies',
            name='contains_skills',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vacancies',
            name='experience',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='vacancies',
            name='published',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='vacancies',
            name='salary_from',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='vacancies',
            name='salary_to',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='vacancies',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]