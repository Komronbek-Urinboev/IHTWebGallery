from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
def index(request):
    photos = Photo.objects.all().order_by('-pub_date')
    return render(request, "main/index.html", {'photos': photos})

def about(request):
    return HttpResponse("<h4>О Нас</h4>")

