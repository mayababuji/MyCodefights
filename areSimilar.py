#!/usr/bin/env python
# -*- coding :utf-8 -*-
def areSimilar(A, B):
    i = 0
    max = 0
    while i < len(A):
        if A[i] != B[i]:
            if A[i] in B:
                j = 0
                while j < len(B):
                    if B[j] == A[i]:
                        if A[j] == B[i]:
                            B[j], B[i] = B[i], B[j]
                            break
                    j += 1
            max += 1
        i += 1
    if max > 1:
        return False
    return True

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [2, 1, 3]
    print areSimilar(a,b)