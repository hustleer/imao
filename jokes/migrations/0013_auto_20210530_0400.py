# Generated by Django 3.1.7 on 2021-05-30 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0012_feedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feedback',
            new_name='Feedbacks',
        ),
    ]
