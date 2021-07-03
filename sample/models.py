from django.db import models
from .const import SELECTION

class Member(models.Model):
    name = models.CharField(verbose_name="氏名", max_length=50)
    age = models.IntegerField(verbose_name="年齢", default=30)
    height = models.IntegerField(verbose_name="年齢",default=170)
    body_weight = models.IntegerField(verbose_name="体重", default=60)
    prefecture =  models.CharField('都道府県', max_length=20,default="東京都", 
                                    null=True, blank=True,choices=SELECTION.TODOUFUKEN)
    def __str__(self):
        return self.name