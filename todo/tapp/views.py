from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TodoForm
from .models import todo
from django.db.models import Q
import datetime


def home(request):
    n = todo.objects.all()
    return render(request, 'home.html', {'t':n, 'now': datetime.datetime.now()})

def entry(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TodoForm()
    return render(request, 'todo.html', {'form':form})

def delete(request,d):
    n = todo.objects.get(id=d)
    n.delete()
    return HttpResponseRedirect('/')

def search(request):
    if request.method == 'POST':
        s = request.POST['search']
        if s:
            sa = todo.objects.filter(Q(label__icontains=s))
            if sa:
                return render(request, 'search.html', {'t': sa,'word':s})
            else:
                return render(request, 'notfound.html')
        else:

            return HttpResponseRedirect('/')

def edit(request,d):
    n = todo.objects.get(id=d)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=n)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TodoForm(instance=n)
    return render(request, 'edit.html', {'form':form})

def detail(request,d):
    c = todo.objects.get(id = d)
    return render(request, 'detail.html', {'name':c})
