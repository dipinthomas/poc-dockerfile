#!/bin/sh
# Start haproxy
haproxy -f /usr/local/etc/haproxy/haproxy.cfg&
# start flask app
python3 flaskapp.py
