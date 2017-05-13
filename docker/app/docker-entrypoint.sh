#!/bin/bash
set -e

until python3 manage.py migrate
do
    echo "Waiting for postgres to be ready..."
    sleep 2
done

python3 manage.py collectstatic --noinput
gunicorn tweetwall.wsgi -b 0.0.0.0:8000 --log-file -