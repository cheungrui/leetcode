#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-26 18:49:24
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
62. Unique Paths
Medium

1137

81

Favorite

Share
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png

Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mat = [[0 for i in range(n)]for j in range(m)]
        mat[0][0] = 1
        for j in range(1, n):
            mat[0][j] = 1
        for i in range(1, m):
            mat[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i-1][j] + mat[i][j-1]
        return mat[m-1][n-1]
        