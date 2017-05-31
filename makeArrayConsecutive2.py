#!usr/bin/env python
# -*-coding:utf-8 -*-
'''
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
each statue having an non-negative integer size. Since he likes to make things perfect, 
he wants to arrange them from smallest to largest so that each statue will be bigger than the previous 
one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out 
the minimum number of additional statues needed.
'''
def makeArrayConsecutive2(statues):
    statues.sort()
    count = []
    for i in range(len(statues)-1):
        if statues[i+1] - statues[i] > 1:
            a = statues[i+1] - statues[i] -1
            count.append(a)
    return sum(count)

if __name__ == '__main__':
    statues = [0,3]
    print makeArrayConsecutive2(statues)
    
    
