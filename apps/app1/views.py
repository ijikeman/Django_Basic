from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import MyForm
from .models import MyModel
from django.urls import reverse_lazy

def create_record(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app1:list_records")
    else:
        form = MyForm()
    return render(request, "app1/create.html", {"form": form})

# def list_records(request):
#     records = MyModel.objects.all()
#     return render(request, "app1/list.html", {"records": records})

# クラスに変更
class ListRecordsView(TemplateView):
    template_name = "app1/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['records'] = MyModel.objects.all()
        return context

def delete_record(request, pk):
    record = MyModel.objects.get(pk=pk)
    record.delete()
    return redirect("app1:list_records")
