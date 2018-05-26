# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class StoreInfo(models.Model):
    stitle=models.CharField(verbose_name='库位名称',max_length=20)

    isPossess=models.BooleanField(default=False)

    spai=models.IntegerField(verbose_name="排(X)")
    slie=models.IntegerField(verbose_name="列(Y)")
    sceng=models.IntegerField(verbose_name="层(Z)")
    class Meta:
        verbose_name = '库位管理'
        verbose_name_plural = verbose_name
        ordering = ['id']
    # gadv=models.BooleanField(default=False)
    def __str__(self):
        return self.stitle.encode('utf-8')