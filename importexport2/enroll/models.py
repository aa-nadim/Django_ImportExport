from django.db import models

# Create your models here.
class ProgileImage(models.Model):
    image=models.FileField(upload_to='profile/%Y/%m/%d')
