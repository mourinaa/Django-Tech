from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('module/', include('modengine.urls')),
    path('product/', include('product_module.urls')),
    path('', lambda request: redirect('module_index')), # redirect root to module index 
    path('accounts/', include('django.contrib.auth.urls')),
]
