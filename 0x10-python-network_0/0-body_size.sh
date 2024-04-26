#!/bin/bash
# Script that sends request to a URL and displays the body size of the response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
