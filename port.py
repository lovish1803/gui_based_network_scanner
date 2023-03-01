#this is the script for ports scan

#!/usr/bin/env python

import subprocess

def port_scan(t):
    result = subprocess.run(['nmap', '-sV', t], capture_output=True, text=True)
    return result.stdout
