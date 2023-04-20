# !/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, nmap automation tool")
print("<------------------------------------------>")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

