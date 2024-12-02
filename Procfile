web: python manage.py migrate && gunicorn --config ./manifests/configs/gunicorn.conf.py
release: python manage.py loaddata initial_data && python manage.py collectstatic --noinput --clear
