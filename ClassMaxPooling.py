#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class MaxPooling:
    '''Class for calculating maximum in each window of size_h x size_v moving accross a rectangular list of numbers
    in steps steps._h x spteps._v. Return a new rectangular list with results. Values which do not fit in a window are not considered'''
    
    def __init__(self, step=(2, 2), size=(2,2)):
        self.__step_h, self.__step_v = step
        self.__size_h, self.__size_v = size
    
    def __call__(self, matrix):
        rows = len(matrix)
        if rows == 0:
            return [[]]
        cols = len(matrix[0]) 
        if not isinstance(matrix, list) or not all(isinstance(el, list) for el in matrix) or len(set(len(row) for row in matrix))!=1 or not all(isinstance(el, (int, float)) for row in matrix for el in row):
            raise ValueError("Wrong foramt: a matrix for MaxPooling must be a rectangular list containing only numbers.")
        
        res_matrix = []
        
        for i in range(0, rows, self.__step_v):
            res = []
            for j in range(0, (cols - self.__size_h + 1), self.__step_h):
                if i + self.__size_v <= rows and j + self.__size_h <= cols:
                    res.append(max([max(matrix[k][j : j + self.__size_h]) for k in range(i, i+self.__size_v)]))
            res_matrix.append(res)
        return [el for el in res_matrix if el]
