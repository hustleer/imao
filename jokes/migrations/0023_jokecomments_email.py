# Generated by Django 3.1.7 on 2021-06-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0022_auto_20210616_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='jokecomments',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
