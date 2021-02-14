from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Perseon

@admin.register(Perseon)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email', 'location')