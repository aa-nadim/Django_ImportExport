# Generated by Django 2.2.17 on 2020-12-03 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventsform',
            old_name='email',
            new_name='error_type',
        ),
        migrations.RenameField(
            model_name='eventsform',
            old_name='name',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='eventsform',
            old_name='phone',
            new_name='time',
        ),
    ]
