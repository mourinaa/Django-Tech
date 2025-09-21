# use Python 3.11
FROM python:3.11-slim

# set work dir
WORKDIR /app

# install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# collect static (in case you use them later)
RUN python manage.py collectstatic --noinput || true

# start app
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
