#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-11 15:46:55
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

import os

"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
"""
class Solution:
    def getisScrambleMatrix(self, length, s1, s2, resultmatrix):
        for i in range(length):
            for j in range(length):
                if s1[i] == s2[j]:
                    resultmatrix[1][i][j] = True
                else:
                    resultmatrix[1][i][j] = False
        #子字符串长度是k
        for k in range(2, length+1):
            for i in range(length-k+1):
                for j in range(length-k+1):
                    if sorted(s1[i:i+k]) != sorted(s2[j:j+k]):
                        resultmatrix[k][i][j] = False
                    else:
                        #m是s1截取的前半段字符串长度
                        for m in range(1, k):
                            if (resultmatrix[m][i][j] and resultmatrix[k-m][i+m][j+m]) or(resultmatrix[m][i][j+k-m] and resultmatrix[k-m][i+m][j]):
                                resultmatrix[k][i][j] = True
                                break
                        else:
                            resultmatrix[k][i][j] = False

    def isScramble(self, s1: str, s2: str) -> bool:
        len_1, len_2 = len(s1), len(s2)
        if len_1 != len_2:
            return False
        if sorted(s1) != sorted(s2):
            return False
        #k对应子字符串长,i是s1中子字符串的开始位置,j是s2中子字符串的开始位置
        resultmatrix = [[[None for j in range(len_2)] for i in range(len_1)] for k in range(len_1+1)]
        self.getisScrambleMatrix(len_1, s1, s2, resultmatrix)
        return resultmatrix[len_1][0][0]