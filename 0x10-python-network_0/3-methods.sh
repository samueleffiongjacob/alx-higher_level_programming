#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 URL"
  exit 1
fi

# Send an OPTIONS request to the provided URL and display the allowed methods
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
