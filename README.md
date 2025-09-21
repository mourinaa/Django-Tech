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
- ERD and Flowchart images in /diagrams/
- Dockerfile, requirements.txt, setup_venv.sh and a script to create demo users and groups.

How to run locally (recommended)
1. Create a virtualenv and install requirements:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

2. Apply migrations and create demo data:
   python manage.py migrate
   python manage.py loaddata demo_fixture.json
   # or run: python manage.py shell < create_demo_data.py  (script included)

3. Run the development server:
   python manage.py runserver

4. Open the app:
   - Engine page (modules list): http://127.0.0.1:8000/module/
   - If you install the product module from that page, the product landing pages appear at:
     http://127.0.0.1:8000/products/

Demo credentials (created by demo fixture / script)
  - Superuser admin: admin123 / Admin123!
  - Manager user: manager123 / Manager123!
  - Regular user: user123 / User123!

Deploying to a public host (if you need a deployed link)
- This environment cannot create a public deployment URL. I included a Dockerfile and instructions
  so you (or I) can deploy to Render, Heroku (container or buildpack), or any VPS. If you want,
  I can provide step-by-step commands for a specific host (Render/Heroku/AWS) — say which one.

Notes / Limitations
- The "Upgrade" feature is implemented by storing dynamic field metadata in the engine and using
  a JSONField on Product to store values for those dynamic fields. This avoids requiring database
  schema migrations in runtime and satisfies the requirement that adding/removing fields be done
  via the Upgrade button.
- The module install/uninstall is implemented logically (toggle in DB). The module code is present
  in the project; installation toggles accessibility and creates demo product data.

Files of interest
- project/settings.py  (Django settings)
- modengine/  (engine app)
- product_module/ (example module app)
- diagrams/erd.png, diagrams/flowchart.png