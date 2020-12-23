from django.db import models


# Create your models here.
class OwnerModel(models.Model):
    class Meta:
        db_table = 'owners'
        verbose_name = 'Владелецу'
        verbose_name_plural = 'Владельцы'

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class PetModel(models.Model):
    class Meta:
        db_table = 'pets'
        verbose_name = 'Питомцу'
        verbose_name_plural = 'Питомцы'

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    type = models.CharField(max_length=20)
    owner = models.ForeignKey(OwnerModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
