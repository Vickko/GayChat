from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.authtoken.views import APIView, AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from login import models

# 用户注册
# User.objects.filter(username="Vickko").delete()


class Signup(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            resp = {
                'data': {
                    'id': '',
                },
                'meta': {
                    'msg': '用户名已被注册',
                    'status': 422,
                },
            }
            return Response(resp,422)
        else:
            user = User.objects.create_user(
                username=username, password=password)
            resp = {
                'data': {
                    'id': user.pk,
                },
                'meta': {
                    'msg': '注册成功',
                    'status': 201,
                },
            }
            return Response(resp)

# 用户登录


class Login(APIView):

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'data': {
                'id': user.pk,
                'token': token.key,
            },
            'meta': {
                'msg': '登录成功',
                'status': 200,
            }
        })

# 用户注销

class Userprofile(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            User.objects.filter(username=username).delete()
            resp = {
                'data': {
                    'id': '',
                },
                'meta': {
                    'msg': '用户注销成功',
                    'status': 201,
                },
            }
            return Response(resp, 201)
        else:
            resp = {
                'data': {
                    'id': '',
                },
                'meta': {
                    'msg': '该用户不存在',
                    'status': 404,
                },
            }
            return Response(resp)

#创建群组
class group_found(APIView):
    def post(self, request, *args, **kwargs):
        owner = request.data.get('owner')
        name = request.data.get('name')
        if models.group.objects.filter(name=name).exists():
            t = models.group.objects.get(name=name)
            resp = {
                'data': {
                    'group_id': t.group_id,
                },
                'meta': {
                    'msg': '群组已存在',
                    'status': 422,
                },
            }
            return Response(resp, 422)
        else:
            group = models.group.objects.create(
                owner=owner, name=name)
            resp = {
                'data': {
                    'group_id': '',
                },
                'meta': {
                    'msg': '创建成功',
                    'status': 201,
                },
            }
            return Response(resp)

