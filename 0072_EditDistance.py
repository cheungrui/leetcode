#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-31 15:04:52
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

import os
"""
72. Edit Distance
Hard

1606

20

Favorite

Share
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

"""
f(i,j)表示word1的前i个数字变为word2的前j个数字的步数;
如果最后一个数相同,那么f(i,j) = f(i-1,j-1)
如果不同的话,分为三种可能:
word1最后一个字母变为word2最后一个字母:f(i,j)=f(i-1,j-1)+1;
word1最后一个字母删去:f(i,j)=f(i-1,j)+1;
word1在最后插入一个字母,这就等效于word2最后一个字母删去:f(i,j)=f(i,j-1)+1;
"""

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1), len(word2)
        #(i,j)代表word1前i个字母到word2前j个字母需要的步数
        resultmartix = [[None for j in range(len2+1)]for i in range(len1+1)]
        resultmartix[0][0] = 0
        for i in range(1, len1+1):
            resultmartix[i][0] = i
        for j in range(1, len2+1):
            resultmartix[0][j] = j
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    resultmartix[i][j] = resultmartix[i-1][j-1]
                else:
                    resultmartix[i][j] = min(resultmartix[i-1][j-1], resultmartix[i-1][j], 
                        resultmartix[i][j-1]) + 1
        return resultmartix[len1][len2]