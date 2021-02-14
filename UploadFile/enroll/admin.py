from django.contrib import admin

# Register your models here.
##python manage.py makemigrations enroll
from .models import EventsForm
admin.site.register(EventsForm)