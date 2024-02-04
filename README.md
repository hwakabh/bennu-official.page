# Bennu Official Homepage
Official Homepage for Bennu

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

## Deployments
As this application have been implemented as basic 3-tiers (Web/App/DB) application with Kubernetes.
For deployment, we expect to run them on GKE, Google Kubernetes Engine, by Google Cloud,
but since we have kubernetes manifests in the repo, and there are few dependencies to GKE, you can also run app with any Kubernetes.

### Deployment dependencies with GKE
As the following kubernetes resources have leveraged with features of Google Cloud, in case you will apply manifests to your non-GKE cluster,
you have to update the values from default, which are defined in `./manifests/*` directory.
- kind: StorageClass
- kind: Ingress

## Application Diagram

![app-digram](./app-diagram.drawio.svg)

***

## Running applications locally

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

### NGINX reverse-proxy
TODO: TBA

***

## License

- This application is licensed by BSD License since basically using Django framework.
