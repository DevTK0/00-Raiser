#!/bin/bash
gunicorn --certfile ./cert/cert.pem --keyfile ./cert/key.pem -b 0.0.0.0:8000 core:app