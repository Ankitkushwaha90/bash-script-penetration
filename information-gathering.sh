#!/bin/bash

# Information Gathering Script for Penetration Testing
# Author: [Your Name]
# Description: This script automates reconnaissance tasks using nslookup, host, dig, and nmap.

# Define target
read -p "Enter target domain or IP: " TARGET

echo "[+] Gathering information for $TARGET..."

# Perform nslookup
echo "\n[+] Running nslookup..."
nslookup $TARGET > nslookup_results.txt
cat nslookup_results.txt

echo "\n[+] Running host command..."
host $TARGET > host_results.txt
cat host_results.txt

# Perform dig queries
echo "\n[+] Running dig command..."
dig $TARGET ANY +noall +answer > dig_results.txt
dig $TARGET MX +noall +answer >> dig_results.txt
dig $TARGET NS +noall +answer >> dig_results.txt
cat dig_results.txt

# Perform an nmap scan
echo "\n[+] Running nmap scan..."
nmap -A -T4 $TARGET > nmap_results.txt
cat nmap_results.txt

# Perform a reverse lookup if it's an IP address
if [[ $TARGET =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "\n[+] Performing reverse lookup..."
    nslookup $TARGET | grep "name =" > reverse_lookup.txt
    cat reverse_lookup.txt
fi

echo "\n[+] Information gathering complete. Results saved in respective files."

# Display next steps
echo "\nNext Steps:"
echo "- Analyze the collected data for potential vulnerabilities."
echo "- Use additional reconnaissance tools if needed (e.g., subfinder, amass)."
echo "- Cross-check results with OSINT sources."
