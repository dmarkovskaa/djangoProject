from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Color(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.color

class Size(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size

class Product(models.Model):
    code = models.CharField(max_length=20, primary_key=True)  # PK
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True, null=True, upload_to='products/')
    category = models.ManyToManyField(Category, blank=True)
    colors = models.ManyToManyField(Color, blank=True)
    sizes = models.ManyToManyField(Size, blank=True)

    def __str__(self):
        return self.name