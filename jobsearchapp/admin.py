from django.contrib import admin
from jobsearchapp.models import Jobs
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Jobs)
class ViewAdmin(ImportExportModelAdmin):
    pass
