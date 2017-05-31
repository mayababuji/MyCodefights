#!/usr/bin/env python
#-*- coding : utf-8 -*-
'''
Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, 
the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.
'''
def alternatingSums(a):
    team1 = a[0::2]
    team2 = a[1::2]
    result = [sum(team1),sum(team2)]
    return result

if __name__ == '__main__':
    a = [50, 60, 60, 45, 70]
    print alternatingSums(a)