from django.contrib import admin
from .models import *


class StoreInfoAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ['stitle','spai','slie','sceng','isPossess']

admin.site.register(StoreInfo,StoreInfoAdmin)

