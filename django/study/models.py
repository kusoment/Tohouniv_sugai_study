from django.db import models
from django.core.validators import FileExtensionValidator
import os

# Create your models here.

class testModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class FileUpload(models.Model):
    title = models.CharField(default='CSV_file', max_length=50)
    upload_dir = models.FileField(upload_to='csv', validators=[FileExtensionValidator(['csv',])])
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def file_name(self):
        """
        相対パスからファイル名のみを取得するカスタムメソッド
        """
        path = os.path.basename(self.upload_dir.name)
        return path

class ProductA(models.Model):
    Date = models.DateField()        #日付
    Revenue = models.IntegerField()  #収益