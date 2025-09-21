from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Module
from django.urls import reverse
from django.contrib import messages
from product_module.models import Product
from django.contrib.auth.decorators import login_required
from decimal import Decimal

def module_index(request):
    Module.objects.get_or_create(name='Product Module', slug='product_module')
    modules = Module.objects.all()
    return render(request, 'modengine/module_index.html', {'modules': modules})

def install_module(request, slug):
    module = get_object_or_404(Module, slug=slug)
    if not module.installed:
        module.installed = True
        # default schema (no extra fields)
        module.schema = []
        module.version = Decimal('1.0')
        module.save()
        # create demo product entries
        Product.objects.get_or_create(name='Demo Product', barcode='0001', defaults={'price': Decimal('9.99'), 'stock': 10})
        messages.success(request, f'Module {module.name} installed.')
    return redirect(reverse('module_index'))

def uninstall_module(request, slug):
    module = get_object_or_404(Module, slug=slug)
    if module.installed:
        module.installed = False
        module.save()
        messages.success(request, f'Module {module.name} uninstalled.')
    return redirect(reverse('module_index'))

def upgrade_module(request, slug):
    module = get_object_or_404(Module, slug=slug)
    # toggle an extra field named 'description'
    schema = module.schema or []
    if 'description' in schema:
        schema.remove('description')
        module.version = module.version + Decimal('0.1')
        module.schema = schema
        module.save()
        messages.success(request, f'Upgrade removed "description" field from {module.name}.')
    else:
        schema.append('description')
        module.version = module.version + Decimal('0.1')
        module.schema = schema
        module.save()
        messages.success(request, f'Upgrade added "description" field to {module.name}.')
    return redirect(reverse('module_index'))
