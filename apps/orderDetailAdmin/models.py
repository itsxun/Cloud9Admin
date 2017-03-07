from django.db import models

from orderAdmin.models import orders
from userAdmin.models import CnUser
from shopAdmin.models import CnShop


# Create your models here.

class orderDetail(models.Model):
    order = models.ForeignKey(orders, verbose_name="订单号")
    user = models.ForeignKey(CnUser,verbose_name="买家")
    shop = models.ForeignKey(CnShop,verbose_name="卖家")
    item_id = models.CharField(max_length=15, verbose_name="商品id", null=False)
    item_title = models.CharField(max_length=15, verbose_name="商品名", null=False)
    item_num = models.IntegerField(verbose_name="商品数量", default=1)
    item_price = models.FloatField(null=False)
    total_price = models.FloatField(null=False)

    class Meta:
        verbose_name = "订单子项详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order

