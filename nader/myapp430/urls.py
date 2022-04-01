from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage),
    path('shop/', views.shop),
    path('ticket/', views.ticket),
    path('shop_list/', views.shop_list, name='shop_list'),
    path('schedule/<int:year>/<str:month>/', views.schedule, name='schedule')
]