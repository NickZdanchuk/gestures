from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm
from  .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Видео',
            {
                'fields': (
                    'video',
                )
            }
        )
    )

admin.site.register(CustomUser, CustomUserAdmin)