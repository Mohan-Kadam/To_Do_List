from django.urls import path
from .import views

urlpatterns =[
    path('', views.task, name='task'),
    path('new/', views.new_task, name='new_task'),
    path('del/<int:pk>/', views.del_task, name='del_task'),
    path('status/<int:pk>/', views.status, name='status'),

]