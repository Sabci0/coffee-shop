from django.urls import path

from . import views

app_name = 'order'

urlpatterns=[
    path('', views.order_view, name='create_order'),
]