#!/bin/bash

# Declare an associative array to store WiFi networks
declare -A wifi_networks

# Get the name of your WiFi interface (replace 'wlan0' if necessary)
interface='wlan0'

# Use iwlist to scan for networks
results=$(sudo iwlist $interface scanning)

# Parse the results
while IFS= read -r line; do
    # Check if this line has the network name (ESSID)
    if [[ $line =~ ESSID:\"(.*)\" ]]; then
        essid=${BASH_REMATCH[1]}
    fi

    # Check if this line has the signal quality
    if [[ $line =~ Quality=([0-9]+)/([0-9]+) ]]; then
        quality=${BASH_REMATCH[1]}
    fi

    # Add the network to the dictionary
    wifi_networks["$essid"]=$quality
done <<< "$results"

# Print the dictionary
for network in "${!wifi_networks[@]}"; do
    echo "Network: $network, Signal Quality: ${wifi_networks[$network]}"
done
