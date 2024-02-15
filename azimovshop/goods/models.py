from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='prof')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    address = models.CharField(max_length=1024, verbose_name='Адрес')
    birthday = models.DateField(verbose_name='Дата рождения', blank=True)
    avatar = models.ImageField(upload_to='profiles',
                               verbose_name='Изображение', blank=True)

    class Meta:
        verbose_name = 'Профиль'

    def __str__(self):
        return str(self.user)


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    description = models.TextField()
    image = models.ImageField(upload_to='category/')
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
    image = models.ImageField(upload_to='product/')
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
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='param')
    value = models.CharField(max_length=200)  # значение

    def __str__(self):
        return f'{self.product} - {self.parameter}'


class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='fav')
    data_add = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='fav')

    class Meta:
        verbose_name = 'Избанное'

    def __str__(self):
        return str(self.product)


class ShoppingCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='cart')
    count = models.PositiveIntegerField(verbose_name="Количество")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='cart')

    class Meta:
        verbose_name = 'Корзина'

    def __str__(self):
        return self.product


class Review(models.Model):
    STARS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Товар')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    text = models.CharField(max_length=512, verbose_name='Текст отзыва')
    rating = models.PositiveIntegerField(choices=STARS, verbose_name='Рейтинг')

    class Meta:
        verbose_name = 'Отзыв'

    def __str__(self):
        return self.text[:30]
