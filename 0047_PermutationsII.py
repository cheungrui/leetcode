#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-21 12:11:34
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
47. Permutations II
Medium

737

38

Favorite

Share
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for i, num in enumerate(nums):
            result = [line[:j]+[num]+line[j:] for j in range(i+1) for line in result]
        result.sort()
        linetmp = None
        tmp = []
        for line in result:
            if line != linetmp:
                tmp.append(line)
            linetmp = line
        result = tmp
        return result
        