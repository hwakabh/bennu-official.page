web: gunicorn --config ./manifests/configs/gunicorn.conf.py
release: python manage.py migrate && python manage.py loaddata initial_data && python manage.py collectstatic --noinput --clear
