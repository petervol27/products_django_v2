from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255)
    popularity = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    image = models.ImageField(null=True, blank=True, default="/placeholder.png")

    def __str__(self):
        return self.name
