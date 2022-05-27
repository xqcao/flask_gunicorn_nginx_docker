#!/bin/sh
gunicorn -w 2 --bind 0.0.0.0:5001 wsgi:app 