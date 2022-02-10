
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import TodoForm
from django .views .generic import ListView
from django . views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class listview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'obj'

class detailview(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'obj1'

class updateview(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'obj1'
    fields = ['name','priority','date']
    def get_success_url(self):
        return reverse_lazy('cbdv',kwargs={'pk':self.object.id})

class deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cblv')



def add(request):
    obj = Task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('task','')
        priority = request.POST.get('priority', '')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'obj':obj})

# def details(request):
#
#     return render(request,'detail.html',)

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    task = Task.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})