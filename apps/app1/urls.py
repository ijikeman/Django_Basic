from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('create/', views.create_record, name='create_record'),
    path('list/', views.list_records, name='list_records'),
    path('delete/<int:pk>/', views.delete_record, name='delete_record'),
]
