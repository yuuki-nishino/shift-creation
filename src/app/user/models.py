from django.db import models
from django.utils import timezone

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length = 50)

    store = models.ForeignKey(Store, on_delete=models.PROTECT, related_name='store')

    created_at = models.DateField('作成日', default=timezone.now)

    class Meta:
        ordering = ('created_at',)

    
    def __str__(self):
        return self.name


class Shift(models.Model):

    date = models.DateField('日付')
    store = models.ForeignKey(Store, on_delete=models.PROTECT, related_name='storename')
    worker1 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='part1')
    worker2 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='part2')
    worker3 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='part3')
    worker4 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='part4')
    created_at = models.DateField('作成日', default=timezone.now)

    def __str__(self):
        return self.date.strftime("%Y/%m/%d") + ',' + str(self.store)


