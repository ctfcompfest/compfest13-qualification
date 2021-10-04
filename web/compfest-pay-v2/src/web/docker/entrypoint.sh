#!/usr/bin/env sh
# Setting environment variables
PGDATA=${PGDATA:-\/var\/lib\/postgresql\/data}
POSTGRES_DB=${POSTGRES_DB:-postgres}
POSTGRES_USER=${POSTGRES_USER:-postgres}
POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-postgres}
export DATABASE_URL=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:5432/${POSTGRES_DB}

# Run postgresql
echo -e "\nRunning postgresql"
su postgres -c "pg_ctl start -D ${PGDATA}"

# Web application initialization
python3 manage.py migrate
python3 manage.py loaddata seed.json

# Run NGINX
nginx

# Test socket folder
echo "Starting $GUNICORN_NAME as `whoami`"
RUNDIR=$(dirname $GUNICORN_SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start gunicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
cd /opt/ctf/app && \
  gunicorn ${GUNICORN_WSGI_MODULE} \
    --name $GUNICORN_NAME \
    --user=$GUNICORN_USER --group=$GUNICORN_GROUP \
    --bind=unix:$GUNICORN_SOCKFILE \
    --log-level=debug \
    --log-file=- \
    -c /gunicorn.conf.py