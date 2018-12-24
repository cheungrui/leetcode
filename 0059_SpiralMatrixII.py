#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-24 10:34:22
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
59. Spiral Matrix II
Medium

339

69

Favorite

Share
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []
        result = [[0 for _ in range(n)] for _ in range(n)]
        left, right, up, down = 0, n-1, 0, n-1
        k=1
        while(left<=right and up<=down):
            for i in range(left, right+1):
                result[up][i] = k
                k += 1
            up += 1
            if left>right or up>down:
                break
            for i in range(up, down+1):
                result[i][right] = k
                k += 1
            right -= 1
            if left>right or up>down:
                break
            for i in range(right, left-1, -1):
                result[down][i] = k
                k += 1
            down -= 1
            if left>right or up>down:
                break
            for i in range(down, up-1, -1):
                result[i][left] = k
                k += 1
            left += 1
        return result