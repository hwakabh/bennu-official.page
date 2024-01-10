web: gunicorn --config gunicorn.conf.py
collect: python manage.py collectstatic --noinput --clear
migrate: python manage.py migrate
seeds: python manage.py loaddata initial_data
createuser: python manage.py createsuperuser --username admin --email noop@example.com --noinput
shell: python manage.py shell
