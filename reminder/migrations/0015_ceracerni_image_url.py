# Generated by Django 5.1 on 2024-10-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0014_ceracerni'),
    ]

    operations = [
        migrations.AddField(
            model_name='ceracerni',
            name='image_url',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
