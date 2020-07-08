#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-31 17:43:13
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
73. Set Matrix Zeroes
Medium

777

153

Favorite

Share
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
                    for k in range(m):
                        if matrix[k][j] != None:
                            matrix[k][j] = 0
                    for k in range(n):
                        if matrix[i][k] != None:
                            matrix[i][k] = 0
