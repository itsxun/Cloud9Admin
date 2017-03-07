from datetime import datetime

from django.db import models

from userAdmin.models import CnUser


# Create your models here.

class order(models.Model):
    buyer = models.ForeignKey(CnUser, verbose_name="买家Id")
    order_time = models.DateField(default=datetime.now, verbose_name="下单时间")
    pay_time = models.DateField(null=True, verbose_name="付款时间")
    deliver_time = models.DateField(null=True, verbose_name="发货时间")
    deliver_address = models.CharField(max_length=100, verbose_name="发货地址", null=False)
    order_price = models.FloatField(null=False)
    postage = models.FloatField(verbose_name="邮费", default=0)

    class Meta:
        verbose_name = "订单预览"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id
