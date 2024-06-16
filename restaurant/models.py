from django.db import models
from django.core.exceptions import ValidationError

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name


class SingletonModel(models.Model):
    numbers = models.IntegerField(default=50)

    def save(self, *args, **kwargs):
        if not self.pk and SingletonModel.objects.exists():
            raise ValidationError('There can be only one Singleton instance')
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise ValidationError('Deletion is not allowed')

    def __str__(self):
        return str(self.numbers)

    class Meta:
        verbose_name = 'Singleton'
        verbose_name_plural = 'Singleton'


class Shake(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
    


class Salat(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
