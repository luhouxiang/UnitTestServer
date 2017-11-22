#!/bin/bash

nohup /opt/kds/anaconda3/envs/python3.5.3/bin/python /opt/kds/mobile-stock/UnitTestServer/manage.py runserver 0.0.0.0:8000 >/dev/null 2>log  &
