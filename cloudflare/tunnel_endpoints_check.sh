#!/bin/bash

# This Bash script performs curl requests to a list of specified URLs to check their HTTP versions.
# It uses an associative array to map each URL to its corresponding HTTP protocol (HTTP/2 or HTTP/3).
# The script includes a function 'perform_curl' to handle the curl requests, outputting each URL with its protocol and the resolved HTTP version.
# Enhanced error handling is implemented to notify if any request encounters an issue.
# This structure allows for easy maintenance and scalability of the script.

# Define URLs and their respective protocols in an associative array
declare -A urls=(
    ["https://region1.v2.argotunnel.com"]="http2"
    ["https://region2.v2.argotunnel.com"]="http2"
    ["https://cftunnel.com"]="http2"
    ["https://h2.cftunnel.com"]="http2"
    ["https://quic.cftunnel.com"]="http3"
)

# Function to perform curl requests
perform_curl() {
    local url=$1
    local protocol=$2

    # Determine the curl flag based on the protocol
    local protocol_flag="--http2" # Default to HTTP/2
    if [ "$protocol" == "http3" ]; then
        protocol_flag="--http3"
    fi

    # Perform the curl request
    curl $protocol_flag -sI "$url" -o/dev/null -w "URL: %{url_effective} | Protocol: $protocol | HTTP Version: %{http_version}\n"
}

# Iterate over associative array
for url in "${!urls[@]}"; do
    perform_curl "$url" "${urls[$url]}"
done

# Check for any curl errors
if [ $? -ne 0 ]; then
    echo "An error occurred during one of the requests."
fi

