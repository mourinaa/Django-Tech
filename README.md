Technical Test Django

What's included
- A Django project implementing a modular engine (modengine) and an example module (product_module).
- Features:
  * /module/  -> engine page that lists available modules and has Install / Upgrade / Uninstall buttons
  * product module landing pages under /products/ (only accessible when installed)
  * Product model (name, barcode, price, stock) + dynamic extra fields handled via "pgrade"
  * Roles: manager (CRUD), user (CRU), public (R)
  * Delete confirmation popup in UI
  * Upgrade operation adds/removes an extra dynamic field (handled without DB schema changes)
- Dockerfile, requirements.txt, setup_venv.sh and a script to create demo users and groups.

How to run locally (recommended)
  - clone this repo with git clone https://github.com/mourinaan/Django-Tech.git
  - create virtual environment. If using Windows, run python -m venv venv and activate with .\venv\Scripts\activate. If using Linux or Mac, run python3 -m venv venv and          activate with source venv/bin/activate.
  - install dependency using pip install -r requirements.txt
  - migrate database with python manage.py migrate.
  - create demo data (user, group, module, product) using python manage.py shell < create_demo_data.py.
  - run server with python manage.py runserver 8080.
  - open in browser http://127.0.0.1:8080/

Demo credentials (created by demo fixture / script)
  - Superuser admin: admin123 / Admin123!
  - Manager user: manager123 / Manager123! (CRUD)
  - Regular user: user123 / User123! (CRU)

This project is also deploy on PythonAnywhere.
You can try it live here: https://yourusername.pythonanywhere.com](https://mourinaan.pythonanywhere.com/

Note

  - default timezone: Asia/Jakarta
  - using Tailwind for UI (simple, clean)
  - module engine support install / upgrade / uninstall
  - public user can see product page but need login for manage
