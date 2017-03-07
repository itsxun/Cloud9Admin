import json

from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
from django.views.generic.base import View

from userAdmin.models import CnUser


class userInfoView(View):
    def get(self, request, userNo):
        user = CnUser.objects.get(id=int(userNo))
        return HttpResponse(json.dumps(user.toDict(),cls=DjangoJSONEncoder,ensure_ascii=False),content_type="application/json;charset=utf-8")

    def post(self):
        return HttpResponse("不支持post方法!")
