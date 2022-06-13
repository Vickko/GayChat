import json

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.authtoken.views import APIView, AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http import JsonResponse
from login import models
from .models import user_user,user_user


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
            return Response(resp, 422)
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


# 创建群组
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


# 添加好友
class add_friend(APIView):
    def post(self, request, *args, **kwargs):
        user_name = request.data.get('user_name')
        friend_name = request.data.get('friend_name')
        if models.user_user.objects.filter(user_name=user_name, friend_name=friend_name).exists():
            resp = {
                'data': {
                    'id': '',
                },
                'meta': {
                    'msg': '关系已存在',
                    'status': 422,
                },
            }
            return Response(resp, 422)
        else:
            user_user = models.user_user.objects.create(
                user_name=user_name, friend_name=friend_name)
            t = models.user_user.objects.get(user_name=user_name, friend_name=friend_name)
            resp = {
                'data': {
                    'user_name': t.user_name,
                    'friend_name': t.friend_name,
                },
                'meta': {
                    'msg': '添加成功',
                    'status': 201,
                },
            }
            return Response(resp)


# 删除好友
class delete_friend(APIView):
    def post(self, request, *args, **kwargs):
        user_name = request.data.get('user_name')
        friend_name = request.data.get('friend_name')
        if models.user_user.objects.filter(user_name=user_name, friend_name=friend_name).exists():
            models.user_user.objects.filter(user_name=user_name, friend_name=friend_name).delete()
            resp = {
                'data': {
                    'id': '',
                },
                'meta': {
                    'msg': '关系删除成功',
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
                    'msg': '关系不存在',
                    'status': 404,
                },
            }
            return Response(resp)


# 申请加入群组
class join_group(APIView):
    def post(self, request, *args, **kwargs):
        user_name = request.data.get('user_name')
        group_name = request.data.get('group_name')
        isOwner = request.data.get('isOwner')
        isAdmin = request.data.get('isAdmin')
        if models.user_group.objects.filter(user_name=user_name, group_name=group_name).exists():
            resp = {
                'data': {
                    'id': '',
                },
                'meta': {
                    'msg': '用户已在群组中',
                    'status': 422,
                },
            }
            return Response(resp, 422)
        else:
            user_group = models.user_group.objects.create(
                user_name=user_name, group_name=group_name, isOwner=isOwner, isAdmin=isAdmin)
            t = models.user_group.objects.get(user_name=user_name, group_name=group_name, isOwner=isOwner,
                                              isAdmin=isAdmin)
            resp = {
                'data': {
                    'user_name': t.user_name,
                    'friend_name': t.group_name,
                    'isOwner': t.isOwner,
                    'isAdmin': t.isAdmin,
                },
                'meta': {
                    'msg': '申请加入群组成功',
                    'status': 201,
                },
            }
            return Response(resp)


# 申请退出群组
class retreat_group(APIView):
    def post(self, request, *args, **kwargs):
        user_name = request.data.get('user_name')
        group_name = request.data.get('group_name')
        if models.user_group.objects.filter(user_name=user_name, group_name=group_name).exists():
            models.user_group.objects.filter(user_name=user_name, group_name=group_name).delete()
            resp = {
                'data': {
                    'id': '',
                },
                'meta': {
                    'msg': '退出群组成功',
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
                    'msg': '用户不在该群组中',
                    'status': 404,
                },
            }
            return Response(resp)
