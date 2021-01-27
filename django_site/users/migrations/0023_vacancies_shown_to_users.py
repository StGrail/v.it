# Generated by Django 3.1.4 on 2021-01-25 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_remove_vacancies_shown_to_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancies',
            name='shown_to_users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]