#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 URL"
  exit 1
fi

# Send a DELETE request to the provided URL and display the response body
curl -sX DELETE "$1"
