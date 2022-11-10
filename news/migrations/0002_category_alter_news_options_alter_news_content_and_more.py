# Generated by Django 4.1 on 2022-08-30 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "title",
                    models.CharField(
                        db_index=True,
                        max_length=150,
                        verbose_name="Наименование категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["title"],
            },
        ),
        migrations.AlterModelOptions(
            name="news",
            options={
                "ordering": ["created_at"],
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
        ),
        migrations.AlterField(
            model_name="news",
            name="content",
            field=models.TextField(blank=True, verbose_name="Контент"),
        ),
        migrations.AlterField(
            model_name="news",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата публикации"
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликовано"),
        ),
        migrations.AlterField(
            model_name="news",
            name="photo",
            field=models.ImageField(
                blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Фото"
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(max_length=150, verbose_name="Наименование"),
        ),
        migrations.AlterField(
            model_name="news",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Обновлено"),
        ),
        migrations.AddField(
            model_name="news",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="news.category",
            ),
        ),
    ]
