#!/usr/bin/env python
import subprocess

target = input("enter the target host: ")
print("Performing the scan... Please wait...")

def vuln_scan(t):
    sub_res = subprocess.call(["sudo", "nmap", "--script", "vuln", t])
    # return fucker
    print(sub_res)
    return sub_res


def fetch_fun(test_str):
    print(".\n.\n.\n.\n.\n.\n.\n.")
    print("The scan is complete...")
    str_lst = test_str.split(" ")

    print("\n\n\n\nprinting the test str...\n\n\n\n")
    print(str_lst)

    res = ""
    for word in str_lst:

        print("\n\n\n\n\nentered the for loop...\n\n\n\n")

        if (word == "VULNERABLE:\n|"):

            print("\n\n\n\nentered the if statement...\n\n\n\n")

            res = str_lst[str_lst.index(word) + 3] + " attack is possible!"
            print(res)


test_str = str(vuln_scan(target))
print("\n\n\ntest_str ka bhi test--", test_str)
fetch_fun(test_str)
