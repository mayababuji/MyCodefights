#!/usr/bin/env python
# -*- coding : utf-8 -*-
def minesweeper(matrix):
    a = [i[:] for i in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            s = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    m,n = i+x,y+j
                    if len(matrix)>m>=0 and len(matrix[0])>n>=0:
                        print i,j,m,n,matrix[m][n],s

                        s += matrix[m][n]
            a[i][j] = s-matrix[i][j] 
    return a

if __name__ == "__main__":
    
    matrix = [[True, False,False],[False, True, False],[False, False, False]]
    print minesweeper(matrix)