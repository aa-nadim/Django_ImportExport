from django.contrib import admin
from django.urls import path

from file.views import profile_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload-csv/', profile_upload, name="profile_upload"),
]