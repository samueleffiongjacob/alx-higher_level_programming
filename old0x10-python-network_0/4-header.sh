#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 URL"
  exit 1
fi

# Send a GET request with the custom header and display the response body
curl -s -H "X-School-User-Id: 98" "$1"
