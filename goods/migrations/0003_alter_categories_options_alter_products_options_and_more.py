# Generated by Django 5.1.1 on 2024-11-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0002_alter_categories_options_categories_name_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="categories",
            options={
                "ordering": ("id",),
                "verbose_name": "Категорию",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterModelOptions(
            name="products",
            options={"verbose_name": "Товар", "verbose_name_plural": "Товарчики"},
        ),
        migrations.AlterField(
            model_name="products",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="goods_images",
                verbose_name="добавление фото",
            ),
        ),
    ]
