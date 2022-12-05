
from django.contrib import admin
from .models import testModel,FileUpload
# Register your models here.
admin.site.register(testModel)
admin.site.register(FileUpload)