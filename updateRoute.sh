#!/bin/sh
/usr/local/bin/python3 -c '
import requests
try:
    requests.post("https://furmannowscrapers.fly.dev:8080/FUNow/api/internal/update-all")
    print("Success:", response.status_code, response.text)
except Exception as e:
    print("Request failed:", e)
'