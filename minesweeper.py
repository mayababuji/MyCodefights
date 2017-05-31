#!/usr/bin/env python
# -*- coding : utf-8 -*-
'''
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]  
'''
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
