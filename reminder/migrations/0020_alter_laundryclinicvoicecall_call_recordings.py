# Generated by Django 5.1 on 2024-11-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0019_laundryclinicvoicecall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laundryclinicvoicecall',
            name='call_recordings',
            field=models.TextField(null=True),
        ),
    ]