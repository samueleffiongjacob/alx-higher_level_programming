#!/bin/bash

# Check if URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 URL"
  exit 1
fi

# Send GET request, follow redirects, and capture the response body and HTTP status code separately
response=$(curl -s -L -w "%{http_code}" -o /tmp/response_body.txt "$1")
status_code=$(echo "$response" | tail -n1)

# Debugging: print the status code and response body to check what was captured
echo "Status code: $status_code"
echo "Response body:"
cat /tmp/response_body.txt

# Check if the status code is 200 and display the body
if [ "$status_code" -eq 200 ]; then
  cat /tmp/response_body.txt
else
  echo "Request failed with status code: $status_code"
fi

# Clean up
rm /tmp/response_body.txt
