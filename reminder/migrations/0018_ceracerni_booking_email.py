# Generated by Django 5.1 on 2024-11-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0017_laundryclinicenglishspeakingcustomerquery_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ceracerni',
            name='booking_email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
