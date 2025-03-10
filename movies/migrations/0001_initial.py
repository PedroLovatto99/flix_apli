# Generated by Django 4.2.15 on 2024-08-29 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("actors", "0001_initial"),
        ("genres", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=500)),
                ("release_date", models.DateField(blank=True, null=True)),
                ("resume", models.TextField(blank=True, null=True)),
                (
                    "actors",
                    models.ManyToManyField(related_name="movies", to="actors.actor"),
                ),
                (
                    "gender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="movies",
                        to="genres.genre",
                    ),
                ),
            ],
        ),
    ]
