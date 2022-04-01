from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Room, Topic, Message, Fan  #to view created tables



# Register your models here.

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)   #view item Room in the admin panel
admin.site.register(Fan)