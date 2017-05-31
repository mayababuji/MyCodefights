#!/usr/bin/env python
# -*-coding : utf-8 -*-
'''
Given a sequence of integers as an array,
 determine whether it is possible to obtain a strictly increasing sequence 
 by removing no more than one element from the array.
'''
def first_bad_pair(sequence):
    """Return the first index of a pair of elements where the earlier
    element is not less than the later elements. If no such pair
    exists, return -1."""
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1

def almostIncreasingSequence(sequence):
    """Return whether it is possible to obtain a strictly increasing
    sequence by removing no more than one element from the array."""
    j = first_bad_pair(sequence)
    if j == -1:
        return True  # List is increasing
    if first_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True  # Deleting earlier element makes increasing
    if first_bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True  # Deleting later element makes increasing
    return False  # Deleting either does not make increasing


# def almostIncreasingSequence(sequence):
#     count = 0
#     for i in range(len(sequence)-1):
#         if not sequence[i] < sequence[i+1]:
#             count +=1
#     if count > 1:
#         return False
#     else:
#         return True
    
if __name__ =='__main__':
    sequence = [1, 2, 3, 4, 5, 3, 5, 6]
    print almostIncreasingSequence(sequence)
    
# count = 0
# sequence = [1, 1, 1, 2, 3]
# for i in range(len(sequence)-1):
#     if not sequence[i] < sequence[i+1]:
#         #del sequence[i]
#         count +=1
# if count > 1:
#     print False
# else:
#     print True
#print count