# Generated by Django 3.1.7 on 2021-06-16 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0020_jokecomments_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jokecomments',
            name='body',
        ),
        migrations.RemoveField(
            model_name='jokecomments',
            name='jokes',
        ),
        migrations.RemoveField(
            model_name='jokecomments',
            name='loves',
        ),
        migrations.RemoveField(
            model_name='jokecomments',
            name='pub_date',
        ),
    ]