#!/bin/bash

echo "RUN Server by gunicron"
gunicorn docker_compose_gui.wsgi -b 0.0.0.0:8000