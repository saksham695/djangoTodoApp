from typing import Text
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from main.models import Todo
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    # pass
    # print(request)
    todo_items = Todo.objects.all().order_by("added_date")
    return render(request, "index.html", {
        "todo_items": todo_items
    })


@csrf_exempt
def addTodo(request):
    current_date = timezone.now()
    todo_text = request.POST["content"]
    created_obj = Todo.objects.create(added_date=current_date, text=todo_text)
    print(created_obj)
    length_of_todos = Todo.objects.all()
    print(length_of_todos)
    return HttpResponseRedirect("/home")


@csrf_exempt
def delete_todo(request, todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/home")
