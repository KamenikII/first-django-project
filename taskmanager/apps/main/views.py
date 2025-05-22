from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Main page', "tasks": tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeless')
        else:
            error = "Fields uncorrected"

    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/create.html', context)


def update(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('homeless')
    else:
        form = TaskForm(instance=task)
    return render(request, 'main/create.html', {'form': form, 'error': '', 'title': 'Edit Task'})


def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('homeless')
