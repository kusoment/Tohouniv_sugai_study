from django.urls import path
from django.shortcuts import render
from random import randint
from study.views import StudyStartView,StudyDetailView,StudyMenuView,StudyListView,csv,call_write_data
#from study.views import StudyCreatView
from study.views import modelform_upload,index,csv_open,csv_index,get_svg
from django.conf import settings
from django.conf.urls.static import static


app_name ='myapp'
urlpatterns = [
  path("study/", StudyStartView, name="study"),
  path("detail/<int:number>", StudyDetailView, name="study-detail"),
  #path("form/",StudyCreatView, name="study-form"),
  path("",StudyMenuView, name="menu"),
  path("list/",StudyListView, name="list"),
  path("file/", csv, name='data_for_csv'),
  path("ajax/", call_write_data, name="call_write_data"),
  path('modelform/', modelform_upload,name="modelform"),
  path('index/', index, name='index'),
  path('csv_index/', csv_index, name='csv_index'),
  path('csv_open/<int:pk>/', csv_open, name='csv_open'),
  path('plot/', get_svg, name='plot'),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)