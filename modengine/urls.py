from django.urls import path
from . import views

urlpatterns = [
    path('', views.module_index, name='module_index'),
    path('install/<slug:slug>/', views.install_module, name='install_module'),
    path('uninstall/<slug:slug>/', views.uninstall_module, name='uninstall_module'),
    path('upgrade/<slug:slug>/', views.upgrade_module, name='upgrade_module'),
]
