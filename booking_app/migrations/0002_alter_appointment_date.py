# Generated by Django 3.2.16 on 2023-02-25 11:38

import booking_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(validators=[booking_app.models.validate_date]),
        ),
    ]
