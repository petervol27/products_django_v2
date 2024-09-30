from django.db import models
from category.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True, default="/placeholder.png")
    category = models.ManyToManyField(
        Category,
        related_name="products",
        blank=True,
    )

    def __str__(self):
        return self.name
