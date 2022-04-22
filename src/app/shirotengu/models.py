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

    store = models.ForeignKey(Store, on_delete=models.PROTECT, related_name='店名')
    start_time = models.DateTimeField('開始時刻')
    end_time = models.DateTimeField('終了時刻')
    worker = models.ForeignKey(User, on_delete=models.PROTECT, related_name='勤務者')
    created_at = models.DateField('作成日', default=timezone.now)

    def __str__(self):
        return self.start_time.strftime("%Y/%m/%d") + ',' + str(self.store)


