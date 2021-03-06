# Generated by Django 3.1.7 on 2021-06-14 15:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0018_auto_20210606_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='JokeComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(default=None, max_length=150)),
                ('loves', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('jokes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jokes.jokes')),
            ],
        ),
    ]
