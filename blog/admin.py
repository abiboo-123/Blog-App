from django.contrib import admin
from . import models
# Register your models here.

class AutherAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status',)

admin.site.register(models.Post, AutherAdmin)