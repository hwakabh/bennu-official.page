# bennu_official
Bennu Official Homepage, with Python Django MTV

This application `bennu_official`, has been implemented on top of Python & Django framework as generic MVC architectures.
- Models with Django ORM (built-in ORM)
- Templates (refered as Views in other frameworks) with Jinja2 (as default one of Django)
- Views (refered as Controllers in other frameworks) with Django's fundamental features

<!-- *** -->
## Run locally
As there are a lot of container engines for your laptop environment, such as [Docker Desktop](https://docs.docker.com/desktop/) or [OrbStack](https://orbstack.dev), \
`bennu_official` has been developed and is generally expected to run in a macOS environment. \
Please follow the official documents of them to install container engines onto your local laptop.

Since `bennu_official` is based on the Python web application platform, [Django](https://github.com/django/django), \
we need to set up Python runtimes aligned to the version defined in `.python-version` for local development. \
For further information of Django framework, please visit [the official documents](https://docs.djangoproject.com/en/5.0/releases/5.0/).

Please set up the runtime with the version above, and the codebase here is generally expected to run with `pyenv` for local development, \
so it is recommended to install `pyenv` first with following [the docs](https://github.com/pyenv/pyenv).

```shell
% pyenv --version
pyenv 2.4.7

% sysctl machdep.cpu.brand_string
machdep.cpu.brand_string: Apple M1
```

There are several options to start local development of this application on your local machine.
- Directly run application
- Run application on docker-compose
- Run application on [KinD](https://kind.sigs.k8s.io)
  - Since there are many options to install KinD, please choose the flavored way for your machine and follow [the official documents](https://kind.sigs.k8s.io/docs/user/quick-start/#installation).

### on your laptop directly
Since Django would use SQLite3 as default backend database, but in this project we have intentionally disabled it for avoiding differences of deployment between production & development. \
Indeed, bennu_official application expects MySQL as its default backend, and there are several options to prepare MySQL database on your laptop.

As described in the previous section, when you have Docker Desktop or OrbStack on your laptop, the easiest way to set up MySQL is:

```shell
# Start only MySQL container with docker-compose
% docker compose up -d mysql
[+] Running 4/4
 ✔ Network bennu-officialpage_default       Created            0.0s
 ✔ Volume "bennu-officialpage_mysql-data"   Created            0.0s
 ✔ Volume "bennu-officialpage_staticfiles"  Created            0.0s
 ✔ Container mysql                          Started
```

Alternatively, if you have already had MySQL database instances with any form factors remotely, you can use it for `bennu_official`. \
For starting Django application in the next step, you need to provide its credentials manually like following syntax:

```shell
# fallback url for local environment
% export JAWSDB_URL='mysql://root:root@0.0.0.0:3306/bennu'
```

For Django application, please note that the default port Django uses is `8000/tcp`. \
(You can also change listen port for application by setting `PORT` environmental variables)

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

In case, when you need to emulate WSGI server same as production on the local environment, you should use `gunicorn` command directly. \
Please visit [Gunicorn repository](https://github.com/benoitc/gunicorn) for more information, including command line options.

```shell
% gunicorn --bind 0.0.0.0:8000 bennu_official.wsgi
```

### on docker-compose
Since pre-built container image has been available in [GitHub Packages](https://github.com/hwakabh/bennu-official.page/pkgs/container/bennu-official.page) of this repository, you can use it for local docker containers. \
By leveraging docker compose, you can start containers, nginx/gunicorn/mysql, all at once.

```shell
# Starts all containers with compose.yaml
% docker compose up -d

% curl -k -X GET localhost:8000/healthz ; echo
{"status": "ok"}

# Clean up containers
% docker compose down --volumes
```

### on kind-cluster
Since production application will be containerized by [Nixpacks](https://nixpacks.com/docs/getting-started) in [Railway](https://railway.com) environment, so we generally recommend to deploy all components on KinD.
(With this option, it is also better without any dependencies onto your machine and decoupled app from runtime with isolation of Kubernetes layer.)

```shell
# Create kind-cluster and validate context
% kind create cluster --config ./manifest/configs/kind.yaml
% kubectl config get-context

# Deploy each controllers for deployment
% kubectl apply -f ./manifests/controllers/

# Deploy all resources (all resources will be deployed into namespace/bennu by Kustomization)
% kubectl apply -k ./manifests
```

With kind-cluster, the application layout should look like above diagram.

![app-digram-kind](./docs/app-diagram-k8s.drawio.svg)

<!-- *** -->
## Caveats
As production application, which you can access via [URL](https://www.bennu-official.page), has been deployed on Heroku, \
there is no reverse-proxy to serve staticfiles or to handle HTTP(S) access dedicately. \
With the production application, the staticfiles have been served by [Whitenoise](https://whitenoise.readthedocs.io/en/stable/index.html), whereas this is not recommended architecture of Django.

For local development, we can deploy NGINX reverse-proxy Pods and shared NFS volumes between NGINX and Gunicorn onto kind-cluster, but this is not actually same architecture as production one.

In the production deployment of WSGI application including Django, the best practice is to deploy a reverse-proxy such as NGINX in front of WSGI server (Gunicorn), \
since WSGI servers are generally not expected to serve static files with production performances. \

In case you would like to deploy reverse-proxy for your environment, as there are a lot of parameters we can use in nginx.conf, for the non-production environment we only need to change the `proxy_pass` parameter to allow NGINX to communicate with Gunicorn.

```conf
# production config (default)
proxy_pass http://django.bennuhp.svc.cluster.local:8000/;

# change for local env (specify gunicorn's address/port on your environment)
proxy_pass http://localhost:8000/;
```

<!-- *** -->
## Tests
In this project, we adopt builtin testing frameworks of Django, based on Python standard libs `unittest`. \
For running unittest in your local environment, you can use:

```shell
# Run all tests in ./tests directory
% python manage.py test -v 2
```

Please note that, some of the features like [`handler404`](https://docs.djangoproject.com/en/5.0/ref/urls/#handler404) or [`handler500`](https://docs.djangoproject.com/en/5.0/ref/urls/#handler500) are used in this application, and these are only applicable to production environment
so that there might be differences between unit test results and production environment.

<!-- *** -->
## License
This application is licensed under the BSD License, since it is generally based on the Django framework.
References: <https://github.com/django/django/blob/main/LICENSE>
