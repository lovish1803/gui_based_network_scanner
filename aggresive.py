#this is the script for the aggresive scan

#!/usr/bin/env python

import subprocess

def agg_scan(t):
    result = subprocess.run(['nmap', '-A', t], capture_output=True, text=True)
    return result.stdout
