from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from modengine.models import Module

def check_installed():
    mod, _ = Module.objects.get_or_create(name='Product Module', slug='product_module')
    return mod.installed

def user_role(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.groups.filter(name='manager').exists():
            return 'manager'
        if request.user.groups.filter(name='user').exists():
            return 'user'
    return 'public'


def index(request):
    if not check_installed():
        return HttpResponse("Module not installed.", status=404)
    products = Product.objects.all()
    role = user_role(request)
    return render(request, 'product_module/index.html', {
        'products': products,
        'role': role,
    })

def product_detail(request, pk):
    if not check_installed():
        return HttpResponse("Module not installed.", status=404)
    product = get_object_or_404(Product, pk=pk)
    role = user_role(request)
    return render(request, 'product_module/detail.html', {
        'product': product,
        'role': role,
    })

@login_required
def create_product(request):
    role = user_role(request)
    if role not in ('manager', 'user'):
        return HttpResponseForbidden("No permission to create.")
    if request.method == "POST":
        Product.objects.create(
            name=request.POST['name'],
            barcode=request.POST['barcode'],
            price=request.POST['price'],
            stock=request.POST['stock']
        )
        messages.success(request, "Product created.")
        return redirect('product_index')
    return render(request, 'product_module/form.html', {'action': 'Create'})

@login_required
def edit_product(request, pk):
    role = user_role(request)
    if role not in ('manager', 'user'):
        return HttpResponseForbidden("No permission to update.")
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.name = request.POST['name']
        product.barcode = request.POST['barcode']
        product.price = request.POST['price']
        product.stock = request.POST['stock']
        product.save()
        messages.success(request, "Product updated.")
        return redirect('product_index')
    return render(request, 'product_module/form.html', {
        'action': 'Edit',
        'product': product
    })

@login_required
def delete_product(request, pk):
    role = user_role(request)
    # only manager can delete product
    if role != 'manager': 
        return HttpResponseForbidden("No permission to delete.")
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted.")
        return redirect('product_index')
    return redirect('product_index')
