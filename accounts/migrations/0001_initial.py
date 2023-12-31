# Generated by Django 4.2.2 on 2023-06-28 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserDetails",
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
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("MALE", "Male"),
                            ("FEMALE", "Female"),
                            ("TRANSGENDER", "Transgender"),
                            ("PREFER NOT TO SAY", "Prefer Not To Say"),
                        ],
                        default="PREFER NOT TO SAY",
                        max_length=255,
                        verbose_name="Gender",
                    ),
                ),
                ("dob", models.DateField(verbose_name="DOB")),
                (
                    "father_name",
                    models.CharField(max_length=255, verbose_name="Father's Name"),
                ),
                (
                    "mother_name",
                    models.CharField(max_length=255, verbose_name="Mother's Name"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
        ),
    ]
