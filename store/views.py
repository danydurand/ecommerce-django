from django.shortcuts import render, redirect, get_object_or_404
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
        products = Product.visibles.filter(category__slug=slug)
        category = Category.visibles.filter(slug=slug).first()
        context = {
            'products': products,
            'category': category,
        }
        return render(request, 'store/products/index.html', context)
    else:
        messages.warning(request, 'No such Category !!')
        return redirect('collections')


def productview(request, cate_slug, prod_slug):
    if Category.visibles.filter(slug=cate_slug) and Product.visibles.filter(slug=prod_slug):
        product = Product.visibles.filter(category__slug=cate_slug, slug=prod_slug).first()
        category = Category.visibles.filter(slug=cate_slug).first()
        context = {
            'product': product,
            'category': category,
        }
        return render(request, 'store/products/detail.html', context)
    else:
        messages.warning(request, 'No such Category and/or Product !!')
        return redirect('collections')
