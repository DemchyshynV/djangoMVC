from django.db import models


# Create your models here.
class PizzaShopModel(models.Model):
    class Meta:
        db_table = 'pizza_shop'
        verbose_name = 'Пицерию'
        verbose_name_plural = 'Пицерии'
        # ordering = ('-name',)
        ordering = ('name',)

    name = models.CharField(max_length=30, verbose_name='Название')
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
    pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
