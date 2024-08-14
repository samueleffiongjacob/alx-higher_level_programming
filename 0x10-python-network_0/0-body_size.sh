#!/bin/bash

# Check if URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 URL"
  exit 1
fi

# Send a request to the URL and display the size of the body of the response in bytes
curl -s "$1" -w '%{size_download}\n' -o /dev/null
