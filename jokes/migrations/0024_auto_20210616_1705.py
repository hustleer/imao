# Generated by Django 3.1.7 on 2021-06-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0023_jokecomments_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jokes',
            name='funney',
            field=models.FloatField(default=None),
        ),
    ]
