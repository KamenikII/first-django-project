from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, RegisterUserForm
from django.contrib.auth import login

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Main page', "tasks": tasks})


def about(request):
    return render(request, 'main/about.html')


@login_required
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


@login_required
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


@login_required
def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('homeless')


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматически логинит после регистрации
            return redirect('homeless')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/register.html', {'form': form})
