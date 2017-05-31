#!/usr/bin/env python
#-*- coding : utf -8 -*-
'''
IPv4 addresses are represented in dot-decimal notation, which
 consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1.

Given a string, find out if it satisfies the IPv4 address naming rules'''
def isIPv4Address(inputString):
    parts = inputString.split(".")
    print parts
    return(len(parts) == 4 and all(part.isdigit() for part in parts) and all(0 <= int(part)<= 255 for part in parts))

if __name__ == "__main__":
    inputString = ".254.255.0"
    print isIPv4Address(inputString)