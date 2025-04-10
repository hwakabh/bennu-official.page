#
# Gunicorn config file
# ref: https://docs.gunicorn.org/en/stable/settings.html
#
wsgi_app = 'bennu_official.wsgi'

# enviroment variables
raw_env = []

# Server Socket
import os
bind = '0.0.0.0:' + os.environ.get('PORT', '8000')

# Worker Processes
worker_class = 'gthread'
workers = 2
threads = 8
keepalive = 0
timeout = 0

# Daemon Mode: run process as foreground
daemon = False

# Logging: output as stdout
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = '-'
loglevel = 'debug'
