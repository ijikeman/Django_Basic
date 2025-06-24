from django.shortcuts import render, redirect
from .forms import MyForm
from .models import MyModel

def create_record(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app1:list_records")
    else:
        form = MyForm()
    return render(request, "app1/create.html", {"form": form})

def list_records(request):
    records = MyModel.objects.all()
    return render(request, "app1/list.html", {"records": records})

def delete_record(request, pk):
    record = MyModel.objects.get(pk=pk)
    record.delete()
    return redirect("app1:list_records")
