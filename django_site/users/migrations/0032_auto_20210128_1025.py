# Generated by Django 3.1.4 on 2021-01-28 07:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_auto_20210126_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancies',
            name='banned_by_users',
            field=models.ManyToManyField(related_name='banned_by_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='skills',
            field=models.CharField(blank=True, max_length=100, verbose_name='Через запятую укажите дополнительные технологии, с которыми у вас есть опыт работы.'),
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='shown_to_users',
            field=models.ManyToManyField(related_name='swown_to_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
