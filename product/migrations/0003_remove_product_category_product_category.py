# Generated by Django 5.1.1 on 2024-09-27 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0001_initial"),
        ("product", "0002_product_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="products", to="category.category"
            ),
        ),
    ]
