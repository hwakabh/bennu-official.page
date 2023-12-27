# Bennu Official Homepage

- Official Homepage for Bennu
  - Formerly: https://bennu-official-hp.herokuapp.com/home/

***

## System Requirements

- Runtime and Component versions
  - Python : 3.11.5
  - Django : 5.0
    - Please follow [the official documents](https://docs.djangoproject.com/en/5.0/releases/5.0/) for further information
- `pip3` is used as package management: version `23.3.2`
- `pyenv`: `2.3.27` on macOS, M1 Apple Silicon

Please setup the runtime with version above, and basically code base here would be expected to run with `pyenv` for local development,
so it is recommended to install `pyenv` first with following [the docs](https://github.com/pyenv/pyenv).

***

## Running and debug locally

### MySQL database
TODO: TBA

### Django application
Please note that the default ports for djang use is `TCP/8000`.
If you have already used TCP/8000, you could specify another one with the command : `python manage.py runserver <YOUR_LOCAL_PORT>`

```bash
# Install dependencies
% pip install -r requirements.txt

# Make migrations
% python manage.py migrate

# Add initial data to MySQL Container
% python manage.py loaddata initial_data

# Start application
% python manage.py runserver
# In case, when you need to emulate production on local, you should use gunicorn
% gunicorn --bind 0.0.0.0:8000 bennu_official.wsgi
```

***

## License

- This application is licensed by BSD License since basically using Django framework.
