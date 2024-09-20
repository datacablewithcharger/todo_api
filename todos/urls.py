from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list_view, name='todo_list'),  
    path('api/todos/', views.api_create_todo, name='api_create_todo'),  
    path('api/todos/<int:id>/', views.api_update_todo, name='api_update_todo'),  
    path('api/todos/delete/<int:id>/', views.api_delete_todo, name='api_delete_todo'),  
    path('create/', views.todo_form, name='create_todo_form'),  
    path('update/<int:id>/', views.todo_form, name='update_todo_form'), 
]
