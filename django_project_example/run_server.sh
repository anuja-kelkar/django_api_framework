#!/usr/bin/env bash
gunicorn django_example_api.wsgi -k gevent -b 127.0.0.1:8000 --workers=1