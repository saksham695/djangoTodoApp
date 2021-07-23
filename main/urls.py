from . import views
from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.home),
    path(r'add_todo/', views.addTodo),
    path(r'delete_todo/<int:todo_id>/', views.delete_todo)
    # path('', TemplateView.as_view(template_name='index.html')),
]
