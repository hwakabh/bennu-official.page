# bennu_official
Bennu Official Homepage, with Python Django MVC


## Prerequisites
As this application, `bennu_official`, has been implemented as basic 3-tiers (Web/App/DB) application with Kubernetes. \
So all the components required for `bennu_official` have already build as container image by [Cloud Native Buildpacks](https://buildpacks.io).

As there is a lot of container engines for your laptop environment such as [Docker Desktop](https://docs.docker.com/desktop/) or [OrbStack](https://orbstack.dev), \
`bennu_official` has been developed and expected generally macOS environment. \
Please follow the official documents of them to install container engines onto your local laptop.


Since `bennu_official` is based on Python web application platform, [Django](https://github.com/django/django), \
we need to setup Python runtimes aligned to version defined in `.python-version` for local development. \
For further information of Django framework, Please visit [the official documents](https://docs.djangoproject.com/en/5.0/releases/5.0/).


Please set up the runtime with version above, and basically code base here would be expected to run with `pyenv` for local development, \
so it is recommended to install `pyenv` first with following [the docs](https://github.com/pyenv/pyenv).

```shell
% pyenv --version
pyenv 2.4.7

% sysctl machdep.cpu.brand_string
machdep.cpu.brand_string: Apple M1
```


## Deployments: Application Diagrams
For deployment, we expect to run them on GKE, Google Kubernetes Engine, by Google Cloud, \
but since we have kubernetes manifests in the repo, and there are few dependencies to GKE, you can also run app with any Kubernetes.

As the following kubernetes resources have leveraged with features of Google Cloud, in case you will apply manifests to your non-GKE cluster, \
you have to update the values from default, which are defined in `./manifests/*` directory.
- kind: StorageClass
- kind: Ingress


![app-digram](./app-diagram.drawio.svg)


## Running locally

### MySQL database
Since Django would use SQLite3 as default backend database, but in this project we have intendedly disabled it for avoiding differences of deployment between production & development. \
Indeed, bennu_official application expects MySQL as its default backend, and there are several options to prepare MySQL database on your laptop.

As described in previous section, when you have Docker Desktop or OrbStack in laptop, the easiest way to setup MySQL is:

```shell
# Start only MySQL container with docker-compose
% docker compose up -d mysql
[+] Running 4/4
 ✔ Network bennu-official_default       Created            0.0s
 ✔ Volume "bennu-official_mysql-data"   Created            0.0s
 ✔ Volume "bennu-official_staticfiles"  Created            0.0s
 ✔ Container mysql                      Started
```

Alternaternatively, if you have already had MySQL database instances with any form factors remotely, you can use it for `bennu_official`. \
For starting Django application in the next step, you need to provide its credentials manually:

```shell
% export MYSQL_DATABASE='****'          # default: bennu
% export MYSQL_USER='****'              # default: root
% export MYSQL_HOSTNAME='****'          # default: mysql
% export MYSQL_ROOT_PASSWORD='****'     # default: root
#-> TBD: this key is actually not for MySQL root user as application requirement
```

### Django application
Please note that the default ports Django uses is `8000/tcp`.

```shell
# Install dependencies
% pip install -r requirements.txt

# Make migrations
% python manage.py migrate

# Add initial data to MySQL Container
% python manage.py loaddata initial_data

# Start application
% python manage.py runserver
# If you have already used 8000/tcp, you could specify another one with the command:
% python manage.py runserver 8001
```

In case, when you need to emulate WSGI server same as production on local environment, you should use gunicorn directly

```shell
% gunicorn --bind 0.0.0.0:8000 bennu_official.wsgi
```

### NGINX reverse-proxy
TODO: TBA


## Using build artifacts

```shell
# Starts all containers with compose.yml
% docker compose up -d
```

By leveraging docker compose, you can start containers, nginx/gunicorn/mysql, all at once. \
So you can easily emulate production application behaviors in your local environment, with pulling build artifacts from [GHCR(GitHub Container Registry) as packages](https://github.com/hwakabh/bennu-official/pkgs/container/bennu-official).

```shell
# Clean up containers
% docker compose down --volumes
```


## Tests
In this project, we adopt builtin testing frameworks of Django, based on Python standard libs `unittest`. \
For running unittest in your local environment, you can use:

```shell
# Run all tests in ./tests directory
% python manage.py test -v 2
```

Please note that, some of the features like [`handler404`](https://docs.djangoproject.com/en/5.0/ref/urls/#handler404) or [`handler500`](https://docs.djangoproject.com/en/5.0/ref/urls/#handler500) are used in this application, and these are only applicable to production environment
so that there might be differences between unit test results and production environment.


## License
This application is licensed by BSD License, since generally based on the Django framework.
References: <https://github.com/django/django/blob/main/LICENSE>
