from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import place
from .models import members
def demo(request):
    obj1=place.objects.all()
    obj2 = members.objects.all()

    return render(request,"index.html",{'result1':obj1,'result2':obj2})