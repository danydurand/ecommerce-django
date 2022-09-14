from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Product

def home(request):
    return render(request, 'store/index.html')


def collections(request):
    categories = Category.visibles.all()
    context = {
        'categories': categories,
    }
    return render(request, 'store/collections.html', context)


def collectionsview(request, slug):
    if Category.visibles.filter(slug=slug):
        products = Product.objects.filter(category__slug=slug)
        category = Category.visibles.filter(slug=slug).first()
        context = {
            'products': products,
            'category': category,
        }
        return render(request, 'store/products/index.html', context)
    else:
        messages.warning(request, 'No such Category !!')
        return redirect('collections')
