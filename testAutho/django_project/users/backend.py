from urllib import request

from django.contrib.auth import login, get_user_model
from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django_project import settings
from users.models import CustomUser

from users import models



class MultiPasswordModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, video=None):
        try:
            user = CustomUser.objects.get(username=username)
            if password == None:
                return user
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

        except CustomUser.DoesNotExist:
            pass








