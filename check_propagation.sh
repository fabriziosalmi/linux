#!/bin/bash

# Define the NS to check
ns="$1"

# Define the list of DNS providers to check
dns_providers=(
    "8.8.8.8"
    "8.8.4.4"
    "1.1.1.1"
    "1.0.0.1"
    "9.9.9.9"
    "149.112.112.112"
    "208.67.222.222"
    "208.67.220.220"
    "64.6.64.6"
    "64.6.65.6"
    "185.228.168.9"
    "185.228.169.9"
    "198.101.242.72"
    "23.253.163.53"
    "156.154.70.1"
    "156.154.71.1"
    "199.85.126.20"
    "199.85.127.20"
    "195.46.39.39"
    "195.46.39.40"
    "216.146.35.35"
    "216.146.36.36"
    "8.26.56.26"
    "8.20.247.20"
    "91.239.100.100"
    "89.233.43.71"
    "dns1.p01.nsone.net"
    "dilbert.ns.cloudflare.com"
)

# Define the ANSI color codes for the output
red="\033[0;31m"
green="\033[0;32m"
reset="\033[0m"

# Loop through the DNS providers and check the NS record
for dns in "${dns_providers[@]}"; do
    echo "Checking $ns on $dns..."

    # Resolve the NS record for the current DNS provider
    result=$(dig +short @$dns NS $ns)

    # Check if the NS record matches the expected value
    if [[ $result == *"dilbert.ns.cloudflare.com"* ]]; then
        echo -e "${green}OK${reset}"
	echo -e "$result"
    else
        echo -e "${red}Mismatch${reset}"
        echo "Expected: dilbert.ns.cloudlfare.com"
        echo "Actual: $result"
    fi

    echo ""
done
