# Generated by Django 5.1 on 2024-10-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0013_alter_laundryclinicspanishspeakingcustomerquery_ai_email_response_spanish'),
    ]

    operations = [
        migrations.CreateModel(
            name='CeraCerni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=50, null=True)),
                ('booking_name', models.CharField(max_length=100, null=True)),
                ('selected_image', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
