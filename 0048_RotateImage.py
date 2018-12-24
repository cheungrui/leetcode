#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-05 15:26:42
# @Author  : Zhang Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
48. Rotate Image
Medium
1115
100


You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
"""
将正方形矩阵顺时针旋转90度，要求不能新建一个矩阵，直接在原来的矩阵上进行更改
"""
"""
可以写成O(1)的空间复杂度，当然时间复杂度还是O(N^2)
首先回顾一下高中的数学知识,二维坐标系上的一点(m,n)顺时针旋转90度后坐标为(n,-m)
矩阵左上角坐标(0,0),右下角坐标(n-1, n-1),x轴向下，y轴向右,和我们平时看到的坐标系只是旋转了一下，
所以矩阵顺时针旋转和我们平时遇到的坐标系顺时针旋转是相同的,高中时的知识仍然适用，
所以矩阵顺时针是围绕点((n-1)/2,(n-1)/2)旋转的,
设矩阵内一点坐标为(a,b),相对于轴心得坐标是(a-(n-1)/2, b-(n-1)/2),
旋转90度以后相对坐标是(b-(n-1)/2, (n-1)/2-a)
所以矩阵内的绝对坐标是(b,n-1-a)
再看矩阵里的点q0,旋转90度到了q1,再旋转90度到了q2,再旋转90度到了q3，再旋转一次就会到达原点，
这四个相对应的点必须一起实现,必须将矩阵这样均匀地分为4份，每四个对应的点分别在这四个区域内，方法很多,
我的方法是对于第i行:0<=i<n-1,取(i,j):i<=j<n-1-i
q0:(i,j)
q1:(j,n-1-i)
q2:(n-1-i,n-1-j)
q3:(n-1-j,i)
"""
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(0,(n-1)//2+1):
            for j in range(i,n-1-i):
                tmp = matrix[i][j]
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]
                # for k in range(4):
                #     i, j = j, n-1-i
                #     matrix[i][j], tmp = tmp, matrix[i][j]

# class Solution:
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: void Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
#         matrix.reverse()
#         for i in range(0,n):
#             for j in range(i):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        