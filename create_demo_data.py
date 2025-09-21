# Run this with: python manage.py shell < create_demo_data.py
from django.contrib.auth.models import User, Group
from modengine.models import Module
from product_module.models import Product

# create groups
g_man, _ = Group.objects.get_or_create(name='manager')
g_user, _ = Group.objects.get_or_create(name='user')

# create users (set usable passwords)
admin, created = User.objects.get_or_create(username='admin123', defaults={'email':'admin@example.com', 'is_superuser':True, 'is_staff':True})
if created:
    admin.set_password('Admin123!')
    admin.save()
manager, created = User.objects.get_or_create(username='manager123', defaults={'email':'manager@example.com'})
if created:
    manager.set_password('Manager123!')
    manager.save()
user, created = User.objects.get_or_create(username='user123', defaults={'email':'user@example.com'})
if created:
    user.set_password('User123!')
    user.save()

manager.groups.add(g_man)
user.groups.add(g_user)

# create module metadata
mod, _ = Module.objects.get_or_create(name='Product Module', slug='product_module')
mod.installed = False
mod.version = 1
mod.schema = []
mod.save()

# create demo product
Product.objects.get_or_create(name='Demo Product', barcode='0001', defaults={'price':9.99, 'stock':10})
print('Demo data created (users/groups/module/product). Credentials:')
print('admin123 / Admin123! (superuser)')
print('manager123 / Manager123! (manager)')
print('user123 / User123! (user)')
