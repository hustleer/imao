# Generated by Django 3.1.7 on 2021-05-22 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0007_uploadjokes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(default=None, max_length=500)),
                ('loves', models.IntegerField(default=0)),
            ],
        ),
    ]
