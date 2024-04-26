#!/bin/bash
# Senda s JSON POST request to a URL and displays the response body
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
