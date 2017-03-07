from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CnUser(AbstractUser):
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(choices=(("male", "男"), ("female", "女")), default="female", max_length=6)
    phone = models.CharField(max_length=11, null=True, blank=True)
    avatar = models.ImageField(upload_to="media/avatar", default="media/avatar/default_user.png", max_length=100)
    rank = models.CharField(max_length=10, verbose_name="会员等级", default="青铜会员")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
