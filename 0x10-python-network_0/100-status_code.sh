#bin/bash
# Senda a request to a URL and displays only the status code of the response
curl -sLw "%{http_code}" -o /dev/null "$1"
