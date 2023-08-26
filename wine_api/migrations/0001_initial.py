# Generated by Django 4.1.6 on 2023-08-26 13:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Wine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("wine_name", models.CharField(max_length=255)),
                ("price", models.IntegerField()),
                ("varietal", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
