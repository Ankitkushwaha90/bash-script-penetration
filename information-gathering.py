#!/usr/bin/env python3

"""
Information Gathering Script for Penetration Testing
Author: [Your Name]
Description: This script automates reconnaissance tasks using nslookup, host, dig, and nmap.
"""

import subprocess
import re

def run_command(command):
    """Runs a shell command and returns its output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def gather_info(target):
    print(f"[+] Gathering information for {target}...\n")
    
    # Run nslookup
    print("[+] Running nslookup...")
    nslookup_result = run_command(f"nslookup {target}")
    print(nslookup_result)
    
    # Run host
    print("\n[+] Running host command...")
    host_result = run_command(f"host {target}")
    print(host_result)
    
    # Run dig queries
    print("\n[+] Running dig command...")
    dig_result = run_command(f"dig {target} ANY +noall +answer")
    dig_result += run_command(f"dig {target} MX +noall +answer")
    dig_result += run_command(f"dig {target} NS +noall +answer")
    print(dig_result)
    
    # Run nmap scan
    print("\n[+] Running nmap scan...")
    nmap_result = run_command(f"nmap -A -T4 {target}")
    print(nmap_result)
    
    # Perform reverse lookup if it's an IP
    if re.match(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', target):
        print("\n[+] Performing reverse lookup...")
        reverse_lookup_result = run_command(f"nslookup {target} | grep 'name ='")
        print(reverse_lookup_result)

if __name__ == "__main__":
    target = input("Enter target domain or IP: ")
    gather_info(target)

    print("\n[+] Information gathering complete.")
    print("\nNext Steps:")
    print("- Analyze the collected data for potential vulnerabilities.")
    print("- Use additional reconnaissance tools if needed (e.g., subfinder, amass).")
    print("- Cross-check results with OSINT sources.")
