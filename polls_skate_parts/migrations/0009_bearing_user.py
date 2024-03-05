# Generated by Django 5.0.2 on 2024-03-05 00:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls_skate_parts", "0008_bearing_truck_wheels"),
        ("polls_user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bearing",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="polls_user.user",
            ),
        ),
    ]