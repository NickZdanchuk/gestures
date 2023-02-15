import base64
import pickle
from urllib import request
import requests
import os
from django.contrib.auth import login, get_user_model
from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pathlib import Path

import json


from django_project import settings
from users.models import CustomUser

from users import models



class MultiPasswordModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, video=None, videoEmbedding=None):
        try:
            user = CustomUser.objects.get(username=username)
            if password == None:
                item_video_Embedding = CustomUser.objects.filter(username=username).first().videoEmbedding

                list_bytes = base64.b64decode(item_video_Embedding)

                list = pickle.loads(list_bytes)
                print(list)

                newVideo = request.POST.get('newVideo')
                print(newVideo)
                newVideo1 = request.POST.get('video1')
                print(newVideo1)

                video = request.POST.get('video')
                print(video)

                for key, value in request.POST.items():
                    print('Key: %s' % (key))
                    print('Value %s' % (value))

                SuperVideo = request.POST.get('SuperVideo')
                print(type(SuperVideo))
                '''
                
                
                #item_video = CustomUser.objects.filter(username=username).first().video

                
                BASE_DIR = Path(__file__).resolve().parent.parent
                #path = os.path.join(BASE_DIR, 'media',item_video.name)

                
                url = "http://127.0.0.1:5000"

                payload = {'name': 'branch'}
                files = [
                    ('content', (
                    'tmp.mp4',
                    # open(path, 'rb'),
                    video.open(mode='rb'),
                    'application/octet-stream'))
                ]
                headers = {}

                response = requests.request("POST", url, headers=headers, data=payload, files=files)

                #print(len(json.loads(response.text)['embedding']))
                '''

                return user
            elif user.check_password(password) and self.user_can_authenticate(user):
                return user

        except CustomUser.DoesNotExist:
            pass








