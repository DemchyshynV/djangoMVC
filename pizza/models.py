from django.db import models
from django.core import validators


# Create your models here.
class PizzaShopModel(models.Model):
    class Meta:
        db_table = 'pizza_shop'
        verbose_name = 'Пицерию'
        verbose_name_plural = 'Пицерии'
        # ordering = ('-name',)
        ordering = ('name',)

    name = models.CharField(max_length=10, verbose_name='Название')
    description = models.TextField(verbose_name="Описание")
    rating = models.FloatField(default=0, verbose_name='Рэйтинг')

    def __str__(self):
        return self.name


class PizzaModel(models.Model):
    class Meta:
        db_table = 'pizza'
        verbose_name = 'Пицу'
        verbose_name_plural = 'Пицы'
        ordering = ('name',)

    name = models.CharField(max_length=30, verbose_name='Назвавине')
    description = models.CharField(max_length=255, verbose_name='Описание')
    cost = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField('Фото', upload_to='pizza/photos', default='', blank=True)
    pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')

    def __str__(self):
        return self.name


def check_first(value: str):
    if value[0].lower() != 'a':
        raise validators.ValidationError('Имя должно начинатся на "a"')


class OrderModel(models.Model):
    class Meta:
        db_table = 'order'

    pizza = models.ForeignKey(PizzaModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, validators=[validators.MinLengthValidator(3, 'Мин 3 символа максимум 30'), check_first])
    phone = models.CharField(max_length=10,
                             validators=[validators.RegexValidator('^[0-9]{10}$', 'Только цифры 10 штук')])
    # def __str__(self):
    #     return self.pizza
