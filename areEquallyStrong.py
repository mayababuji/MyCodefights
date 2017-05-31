#!/usr/bin/env python
# -*- coding : utf -8 -*-
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return (yourLeft == friendsLeft or yourLeft == friendsRight) and (yourRight == friendsLeft or yourRight == friendsRight)
    
if __name__ == "__main__":
    yourLeft = 15
    yourRight = 5
    friendsLeft = 5
    friendsRight = 15
    print areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight)
    
    
    