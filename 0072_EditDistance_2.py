#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-31 16:30:07
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

import os
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:
            return 0
        len1, len2 = len(word1), len(word2)
        #(i,j)代表word1前i个字母和word2前j个字母到word1,word2要的步数
        resultmartix = [[None for j in range(len2+1)]for i in range(len1+1)]
        resultmartix[len1][len2] = 0
        queue = [(len1, len2)]
        time = 0
        while 1:
            tmp = []
            if resultmartix[0][0] != None:
                return resultmartix[0][0]
            for i, j in queue:
                while i and j and word1[i-1] == word2[j-1]:
                    resultmartix[i-1][j-1] = time
                    i, j = i-1, j-1
                if i and resultmartix[i-1][j] == None:
                    resultmartix[i-1][j] = time + 1
                    tmp.append((i-1, j))
                if j and resultmartix[i][j-1] == None:
                    resultmartix[i][j-1] = time + 1
                    tmp.append((i, j-1))
                if i and j and resultmartix[i-1][j-1] == None:
                    resultmartix[i-1][j-1] = time + 1
                    tmp.append((i-1, j-1))
            time += 1
            queue = tmp
