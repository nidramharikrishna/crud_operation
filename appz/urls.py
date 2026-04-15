from django.urls import path
from appz.views import stu_create,stu_read,stu_delete,stu_update

urlpatterns = [
    path('create', stu_create,name='stu_create'),
    path('',stu_read,name='stu_list'),
    path('update/<int:id>/',stu_update,name='stu_update'),
    path('delete/<int:id>/',stu_delete,name='stu_delete'),
    ]