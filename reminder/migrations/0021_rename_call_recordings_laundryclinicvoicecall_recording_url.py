# Generated by Django 5.1 on 2024-11-08 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0020_alter_laundryclinicvoicecall_call_recordings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laundryclinicvoicecall',
            old_name='call_recordings',
            new_name='recording_url',
        ),
    ]