# Generated by Django 5.1.3 on 2024-11-22 00:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="JournalEntry",
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
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("tags", models.CharField(blank=True, max_length=255)),
                (
                    "mood",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("happy", "Happy"),
                            ("sad", "Sad"),
                            ("neutral", "Neutral"),
                            ("anxious", "Anxious"),
                            ("angry", "Angry"),
                        ],
                        max_length=50,
                    ),
                ),
                ("media", models.FileField(blank=True, null=True, upload_to="media/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_public", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="journal_entries",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
