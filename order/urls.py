from django.urls import path

from . import views

app_name = 'order'

urlpatterns=[
    path('', views.order_view, name='create_order'),
    path('detail/', views.order_detail_view, name='create_order_detail'),
]