# Generated by Django 3.1.7 on 2021-04-08 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hot_votes', models.IntegerField()),
                ('not_votes', models.IntegerField()),
            ],
        ),
    ]
