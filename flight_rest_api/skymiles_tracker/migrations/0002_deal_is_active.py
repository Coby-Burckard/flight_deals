# Generated by Django 2.2.2 on 2019-07-29 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skymiles_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
