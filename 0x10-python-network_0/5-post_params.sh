#!/bin/bash
# Sends a POST request with parameters to a URL and displays the response body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
