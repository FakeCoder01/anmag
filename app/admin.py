from django.contrib import admin
from .models import AnonUser, Message
# Register your models here.


admin.site.register(AnonUser)
admin.site.register(Message)
