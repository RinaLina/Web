#!/bin/bash
cd /root/books
gunicorn -b 127.0.0.1:8006 dz.wsgi:application
