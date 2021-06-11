# Generated by Django 3.1.7 on 2021-03-27 17:06

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWithFileField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('filez', models.FileField(upload_to='jokes/static/jokes/images')),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='user/static/user/profile_pics')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(default=None, max_length=50, null=True)),
                ('middle_name', models.CharField(default=None, max_length=50, null=True)),
                ('last_name', models.CharField(default=None, max_length=50, null=True)),
                ('preferred_categories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=250), default=None, null=True, size=None)),
                ('email', models.EmailField(max_length=254)),
                ('her_country', models.CharField(default=None, max_length=60, null=True)),
                ('phone_number', models.BigIntegerField(default=0)),
                ('relligion', models.CharField(max_length=50)),
                ('profile_url', models.CharField(default='', max_length=100)),
                ('profile_pic', models.FileField(upload_to='user/static/user/images')),
            ],
        ),
    ]