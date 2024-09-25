from django.contrib import admin
from . import models
# Register your models here.

class AutherAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'seen',)

admin.site.register(models.Contact, ContactAdmin)

admin.site.register(models.Post, AutherAdmin)