# Generated by Django 3.1.4 on 2021-01-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210122_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancies',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
