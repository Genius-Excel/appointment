# Generated by Django 5.1 on 2024-10-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0008_laundryclinicenglishspeakingcustomerquery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laundryclinicenglishspeakingcustomerquery',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
