from django.urls import path
from .views import upload_file_virw

app_name='csvs'

urlpatterns=[
    path('',upload_file_virw, name='upload-view'),
]