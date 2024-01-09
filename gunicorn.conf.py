#
# Gunicorn config file
#
wsgi_app = 'bennu_official.wsgi'

# enviroment variables
raw_env = []

# Server Socket
bind = '0.0.0.0:8000'

# Worker Processes
workers = 2

# Daemon Mode: run process as foreground
daemon = False

# Logging: output as stdout
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = '-'
loglevel = 'info'
