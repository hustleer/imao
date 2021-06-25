# Generated by Django 3.1.7 on 2021-06-24 11:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0026_auto_20210619_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='jokes',
            name='joke_type',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=150), default=None, null=True, size=None),
        ),
    ]
