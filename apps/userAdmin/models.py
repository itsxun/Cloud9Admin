from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CnUser(AbstractUser):
    birthday = models.DateField(verbose_name="出生日期", null=True, blank=True)
    gender = models.CharField(choices=(("male", "男"), ("female", "女")), default="male", max_length=6,verbose_name="性别")
    phone = models.CharField(max_length=11, null=True, blank=True,verbose_name="手机号")
    avatar = models.ImageField(upload_to="media/avatar", default="media/avatar/default_user.png", max_length=100, verbose_name = "头像")
    rank = models.CharField(max_length=10, verbose_name="会员等级", default="青铜会员")

    class Meta:
        verbose_name = "用户详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def toDict(self):
        json = {}
        for f in self._meta.concrete_fields:
            if f.name=="avatar":
                continue
            json[f.name]=f.value_from_object(self)
        return json