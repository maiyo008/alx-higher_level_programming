#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
url="$1"; curl -sI $url | grep -i Content-length |awk '{print $2}'
