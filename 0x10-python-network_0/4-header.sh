#!/bin/bash
# Sends a GET request with a custom header & displays the response body
curl -sX GET -H "X-School-User-Id:98" "$1"
