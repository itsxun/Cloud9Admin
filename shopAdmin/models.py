from django.db import models
from datetime import datetime


from userAdmin.models import CnUser
# Create your models here.

class CnShop(models.Model):
	shop_id=models.CharField(max_length=20,verbose_name="店铺Id",primary_key=True)
	shop_name=models.CharField(max_length=10,verbose_name="店铺名称",null=False)
	sells_type=models.CharField(max_length=10,verbose_name="商品类型",null=False)
	user=models.ForeignKey(CnUser,verbose_name="店主id",null=False);
	legal_name=models.CharField(max_length=10,verbose_name="法人姓名",null=False)
	legal_id=models.CharField(max_length=20,verbose_name="法人身份证号码",null=False)
	address=models.CharField(max_length=100,verbose_name="法人联系地址",null=False)
	avatar=models.ImageField(upload_to="media/avatar",default="media/avatar/default_shop.png",max_length=100);
	rank=models.CharField(max_length=10,verbose_name="会员等级",default="一星卖家")
	shop_ave_score=models.CharField(max_length=5,verbose_name="店铺打分",default=0)
	service_score=models.CharField(max_length=5,verbose_name="服务打分",default=0)
	logistics_score=models.CharField(max_length=5,verbose_name="物流打分",default=0)
	is_active=models.BooleanField(default=False,verbose_name="店铺状态",null=False)
	date_joined=models.DateField(default=datetime.now,verbose_name="店铺创建时间",null=False)

	class Meta:
		verbose_name="店铺信息";
		verbose_name_plural=verbose_name;

	def __str__(self):
		return self.shop_name;