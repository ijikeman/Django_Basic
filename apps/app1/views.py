from django.shortcuts import render, redirect
from .forms import MyForm # forms.pyのMyFormクラスを利用
from .models import MyModel # models.pyのMyModelクラスを利用
from django.views.generic import TemplateView # TemplateViewを継承してviewをクラス形式に変更
from modules.email_utils import EmailUtils

# 関数型
def create_record(request):
    if request.method == "POST":
        form = MyForm(request.POST) # formのデータを取り込み
        if form.is_valid(): # .is_valid標準関数
            form.save() # .save標準関数
            return redirect("app1:list_records") # app1/urls.pyのname=list_recordsへ飛ぶ
    else:
        form = MyForm() # MyFormのフォームを取り込む
    return render(request, "app1/create.html", {"form": form}) # formを渡してrenderingする

# def list_records(request):
#     records = MyModel.objects.all()
#     return render(request, "app1/list.html", {"records": records})

# クラスに変更
class ListRecordsView(TemplateView):
    template_name = "app1/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # 親クラスのget_context_dataを呼び出し、基本のコンテキストを取得
        context['records'] = MyModel.objects.all() # recordsというキーでMyModelの全オブジェクトをコンテキストに追加
        return context # コンテキストを返す

def delete_record(request, pk):
    record = MyModel.objects.get(pk=pk)
    record.delete()
    return redirect("app1:list_records")

def check_records(request):
    selected_records = request.POST.getlist('selected_records')
    selected_objects = MyModel.objects.filter(pk__in=selected_records)
    return render(request, 'app1/check.html', {'selected_records': selected_objects})
