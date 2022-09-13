from django.shortcuts import render
from .models import Category

def home(request):
    return render(request, 'store/index.html')


def collections(request):
    categories = Category.visibles.all()
    context = {
        'categories': categories,
    }
    return render(request, 'store/collections.html', context)

