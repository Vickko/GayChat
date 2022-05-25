from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.authtoken.views import APIView, AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

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
