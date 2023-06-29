from .models import Todo
from django.template import loader
from django.http import HttpResponse


def index(request):
    todos_list = Todo.objects.all()
    template = loader.get_template("todos/index.html")
    context = {
        'todos_list': todos_list
    }
    return HttpResponse(template.render(context, request))