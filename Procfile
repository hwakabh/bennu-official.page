web: gunicorn --config gunicorn.conf.py
migrate: python manage.py migrate && python manage.py collectstatic --noinput --clear
createuser: python manage.py createsuperuser --username admin --email noop@example.com --noinput
