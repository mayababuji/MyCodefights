#!/usr/bin/env python
# -*- coding :utf-8 -*-
'''
Correct variable names consist only of Latin letters, 
digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.
'''

# def variableName(name):
#     return not name[0].isdigit() and all(c.isalnum() or c == '_' for c in name)
#isidentifier works only in python3
# def variableName(name):
#     return name.isidentifier()

  
# import string
# def variableName(name):
#     return len(filter(lambda x: x not in ["_"]+list(string.ascii_letters)+list(string.digits), str(name))) < 1 and (name[0].isalpha() or name[0] == "_")


import re
# def variableName(name):
#     pattern = re.compile("^[a-zA-Z_]{1}\w*$")
#     return bool(pattern.match(name))


def variableName(name):
    return re.match('^[a-zA-Z_]+[a-zA-Z0-9_0]*$', name) is not None

if __name__ == "__main__":
    name = "2w2"
    print variableName(name)