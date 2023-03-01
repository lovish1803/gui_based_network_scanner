#this is the script for deep scan

#!/usr/bin/env python

import subprocess

def deep_scan(t):
    msg()
    result = subprocess.run(["sudo", "nmap", "--script", "vuln", t], capture_output=True, text=True)
    return result.stdout

def msg():
    return "please wait deep scan will take 20-25 minutes ....."