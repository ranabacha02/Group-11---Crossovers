from django.contrib import admin

# Register your models here.
from .models import *



admin.site.register(fan)
admin.site.register(trainee)
admin.site.register(coach)

admin.site.register(ShopItem)
admin.site.register(OrderShop)
admin.site.register(Tag)

admin.site.register(ticket)
admin.site.register(OrderTicket)