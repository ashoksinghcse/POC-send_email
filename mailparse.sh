#!/bin/bash
cd /home/ashoksingh/projects/POC-send_email

source  venv/bin/activate
pgrep -f test.py || python3 test.py
exit 0
