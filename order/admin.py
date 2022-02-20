from django.contrib import admin

# Register your models here.
from order.models import User, UserDetail

admin.site.register(User)
admin.site.register(UserDetail)