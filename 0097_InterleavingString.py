#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-10 08:55:29
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

import os
"""
97. Interleaving String
Hard

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        resultmatrix = [[None for j in range(l2+1)] for i in range(l1+1)]
        resultmatrix[0][0] = True
        for i in range(1, l1+1):
            resultmatrix[i][0] = resultmatrix[i-1][0] and (s1[i-1]==s3[i-1])
        for j in range(1, l2+1):
            resultmatrix[0][j] = resultmatrix[0][j-1] and (s2[j-1]==s3[j-1])
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                e1, e2, e3 = s1[i-1], s2[j-1], s3[i+j-1]
                if e3 == e1 and e3 == e2:
                    resultmatrix[i][j] = resultmatrix[i][j-1] or resultmatrix[i-1][j]
                elif e3 == e1:
                    resultmatrix[i][j] = resultmatrix[i-1][j]
                elif e3 == e2:
                    resultmatrix[i][j] = resultmatrix[i][j-1]
                else:
                    resultmatrix[i][j] = False
        return resultmatrix[l1][l2]
