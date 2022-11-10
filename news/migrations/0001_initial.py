# Generated by Django 4.1 on 2022-08-30 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=150, verbose_name="")),
                ("content", models.TextField(blank=True, verbose_name="")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name=""),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="")),
                (
                    "photo",
                    models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name=""),
                ),
                ("is_published", models.BooleanField(default=True, verbose_name="")),
            ],
            options={"verbose_name": "Новость", "verbose_name_plural": "Новости",},
        ),
    ]
