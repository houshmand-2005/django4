from django.contrib import admin

# Register your models here.
from .models import Room,topic,Messages
admin.site.register(Room)
admin.site.register(topic)
admin.site.register(Messages)
