# Generated by Django 4.1.3 on 2023-03-13 09:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True, choices=[("M", "Male"), ("F", "Female")], max_length=1
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=13,
                validators=[
                    django.core.validators.RegexValidator("^010-?[1-9]/d3-?/d4$")
                ],
            ),
        ),
    ]
