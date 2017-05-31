#!/usr/bin/env python
# -*- coding : utf -8 -*-
'''
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

Example

For yourLeft = 10, yourRight = 15, friendsLeft = 15 and friendsRight = 10, the output should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
'''
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return (yourLeft == friendsLeft or yourLeft == friendsRight) and (yourRight == friendsLeft or yourRight == friendsRight)
    
if __name__ == "__main__":
    yourLeft = 15
    yourRight = 5
    friendsLeft = 5
    friendsRight = 15
    print areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight)
    
    
    
