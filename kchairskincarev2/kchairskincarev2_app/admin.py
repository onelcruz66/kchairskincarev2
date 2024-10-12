from django.contrib import admin
from .models import AppointmentRequest, MessageRequest
# Register your models here.

admin.site.register(AppointmentRequest)
admin.site.register(MessageRequest)