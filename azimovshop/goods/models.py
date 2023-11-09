from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Parameter(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    count = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    old_price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    parameters = models.ManyToManyField(Parameter,
                                        through='ParametersInProduct')

    def __str__(self):
        return self.name


class ParametersInProduct(models.Model):
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.product} - {self.parameter}'
