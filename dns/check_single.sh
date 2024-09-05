#!/bin/bash

# Define the FQDN to check
fqdn="$1"
fqdn_type="$2"

# Define the DNS servers to check against
nameservers=(
    "dns1.p01.nsone.net"
    "dilbert.ns.cloudflare.com"
)

# Define the ANSI color codes for the output
red="\033[0;31m"
orange="\033[0;33m"
yellow="\033[1;33m"
green="\033[0;32m"
reset="\033[0m"

# Loop through the DNS servers and check the resolution of the FQDN
for ns in "${nameservers[@]}"; do
    echo "Checking $fqdn on $ns..."

    # Resolve the FQDN using the current DNS server
    result=$(dig +short @$ns $fqdn $fqdn_typ $fqdn_type)

    # Compare the resolution to the first result (if any)
    if [[ -z $result ]]; then
        echo "Unable to resolve $fqdn on $ns"
        continue
    elif [[ -z $expected ]]; then
        expected=$result
        continue
    elif [[ $result == $expected ]]; then
        echo -e "${green}OK${reset}"
        echo -e "$result"
    elif [[ $result == *"$expected"* ]]; then
        echo -e "${yellow}Similar${reset}"
    elif [[ $result != *"$expected"* ]]; then
        echo -e "${orange}Different${reset}"
        echo "Expected: $expected"
        echo "Actual: $result"
    fi
done

# Check if there were any strictly different results
for ns in "${nameservers[@]}"; do
    result=$(dig +short @$ns $fqdn)
    if [[ $result != $expected ]]; then
        echo -e "${red}Strictly Different Result Detected On $ns!${reset}"
        echo "Expected: $expected"
        echo "Actual: $result"
        exit 1
    fi
done
