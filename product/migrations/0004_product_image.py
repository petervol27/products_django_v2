# Generated by Django 5.1.1 on 2024-09-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_remove_product_category_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, default="/placeholder.png", null=True, upload_to=""
            ),
        ),
    ]
