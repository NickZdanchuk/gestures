from django.urls import path, re_path, include
from django.views.generic import TemplateView

from .views import *

urlpatterns = [

    #path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]