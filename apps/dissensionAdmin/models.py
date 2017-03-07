from django.db import models

from datetime import datetime

from userAdmin.models import CnUser
from shopAdmin.models import CnShop


# Create your models here.
class dissension(models.Model):
    order_id = models.ForeignKey(verbose_name="订单号")
    buyer = models.ForeignKey(CnUser, verbose_name="买家", null=False)
    seller = models.ForeignKey(CnShop, verbose_name="卖家", null=False)
    issue_time = models.DateField(default=datetime.now, verbose_name="纠纷时间")
    buyer_desc = models.CharField(verbose_name="买家描述", null=False,max_length=100)
    seller_desc = models.CharField(verbose_name="卖家描述", default="", max_length=100)

    class Meta:
        verbose_name = "纠纷详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.buyer.username + '——>' + self.seller.shop_name
