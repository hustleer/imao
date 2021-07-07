# Generated by Django 3.1.7 on 2021-06-16 07:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0021_auto_20210616_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='jokecomments',
            name='body',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='jokecomments',
            name='jokes',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='jokes.jokes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jokecomments',
            name='loves',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jokecomments',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]