# Generated by Django 4.1.5 on 2024-08-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientappointment',
            name='selected_property_address',
            field=models.TextField(default='Not applicable'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientappointment',
            name='selected_property',
            field=models.TextField(null=True),
        ),
    ]