from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from random import randint
from .models import testModel,Document,FileUpload
from .forms import StudyFormClass,DocumentForm
import os
import csv
from .application.data_for_csv import write_csv,return_text
from django_pandas.io import pd
#from .application import chana
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io

# Create your views here.
def StudyStartView(request):
	template_name = "study/study"
	return render(request, "study/start.html")

def StudyDetailView(request,number):
	tamplate_name="study/study-detail.html"
	random_int= randint(1,10)
	ctx = {
		"random_number": random_int,
		"number":number,
	}
	return render (request, tamplate_name,ctx)

"""
def StudyCreatView(request):
	template_name="study/study-form.html"
	obj=testModel.objects.get(pk=pk)
	initial_values = {"title":obj.title, "content":obj.content}
	
	form=StudyFormClass(request.POST or initial_values)
	ctx={"form":form}

	if form.is_valid():
		title= form.cleaned_data["title"]
		content = form.cleaned_data["content"]
		obj=testModel(title=title, content=content)
		obj.save()
		print(title)
		print(content)

	return render(request, template_name, ctx)
"""


def StudyMenuView(request):
	tamplate_name="study/menu.html"
	return render(request, tamplate_name)

def StudyListView(request):
	tamplate_name = "study/study-list.html"
	ctx = {}
	qs = testModel.objects.all()
	ctx["object_list"] = qs

	return render(request, tamplate_name, ctx)



#こっから付け足したやつ。
def csv(request):
	tamplate_name="study/csv.html"
	return render(request,tamplate_name,)

def call_write_data(request):
	if request.method == 'GET':
		#メソッド呼ぶ
		#ajaxで送信したデータのなかで、"input_data"を指定する。
		write_csv(request.GET.get("input_data"))
		data = return_text()
		return HttpResponse(data)


#file_upload用のやつ
def modelform_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    else:
        form = DocumentForm()
    return render(request, 'study/file_upload.html', {
        'form': form
    })

#FORMアップロード保存のやつ（うえとおなじー）
def index(request):
	documents = Document.objects.all()
	return render(request, 'study/index.html',{'documents':documents})




def csv_index(request):
	file_obj = FileUpload.objects.all()
	context = {
		'file_obj':file_obj,
	}
	return render(request, 'study/csv_index.html', context)


def csv_open(request, pk):
    """
    詳細ページ
    """
    file_value = get_object_or_404(FileUpload, id=pk)
    try:
        # utf-8に対応
        df = pd.read_csv(file_value.upload_dir.path, index_col=0)
    except UnicodeDecodeError:
        # cp932に対応
        df = pd.read_csv(file_value.upload_dir.path, index_col=0, encoding='cp932')
    context = {
            'file_value': file_value,
            'df': df,
    }
    return render(request, 'study/csv_open.html', context)

#グラフ作成
def setPlt():
    x = ["07/01", "07/02", "07/03", "07/04", "07/05", "07/06", "07/07"]
    y = [3, 5, 0, 5, 6, 10, 2]
    plt.bar(x, y, color='#00d5ff')
    plt.title(r"$\bf{Running Trend  -2020/07/07}$", color='#3407ba')
    plt.xlabel("Date")
    plt.ylabel("km")

# SVG化
def plt2svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

# 実行するビュー関数
def get_svg(request):
    setPlt()  
    svg = plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response