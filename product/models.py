from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    price = models.DecimalField(max_digits=50, decimal_places=2)

    def __str__(self):
        return self.title
