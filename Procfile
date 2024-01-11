web: python manage.py collectstatic --noinput --clear && gunicorn --config gunicorn.conf.py
migrate: python manage.py migrate
seeds: python manage.py loaddata initial_data
createuser: python manage.py createsuperuser --username admin --email noop@example.com --noinput
shell: python manage.py shell
manage: python manage.py
