#!/bin/bash
cd /home/ashoksingh/projects/POC-send_email

source  venv/bin/activate
pgrep -f subscriber.py || python3 subscriber.py
exit 0
