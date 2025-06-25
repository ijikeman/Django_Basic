from django.urls import path
from . import views

app_name = 'app1' # urls.pyをアプリ側で実装する為、app_nameの定義が必要

urlpatterns = [
    path('create/', views.create_record, name='create_record'),
    path('list/', views.ListRecordsView.as_view(), name='list_records'),
    path('delete/<int:pk>/', views.delete_record, name='delete_record'),
]
