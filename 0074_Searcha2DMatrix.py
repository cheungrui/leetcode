#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-02 09:47:42
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
74. Search a 2D Matrix
Medium

616

77

Favorite

Share
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [ 
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        cowlen, rowlen = len(matrix), len(matrix[0])
        left, right = 0, cowlen*rowlen -1
        smallnum, bignum = matrix[0][0], matrix[cowlen-1][rowlen-1]
        while(left<=right):
            mid = (left + right)//2
            cow, row = divmod(mid, rowlen)
            midnum = matrix[cow][row]
            if midnum == target:
                return True
            elif midnum < target:
                left, smallnum = mid+1, midnum
            else:
                right, bignum = mid-1, bignum
        return False


