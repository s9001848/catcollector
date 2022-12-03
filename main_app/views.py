from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat

# Create your views here.
def index(request):
    cats = list(Cat.objects.all())
    return render(request, "index.html", { 'cats': cats })
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def cats_index(request):
    cats = list(Cat.objects.all())
    return render(request, 'cats/index.html', { 'cats': cats })

def cats_show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)

    return render(request, 'cats/show.html', { 'cat': cat })