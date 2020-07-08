#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-05 15:28:39
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
90. Subsets II
Medium

693

37

Favorite

Share
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        nums.sort()
        for num in nums:
            result.extend([i+[num] for i in result])
        result.sort()
        itmp = None
        tmp = []
        for i in result:
            if i != itmp:
                tmp.append(i)
            itmp = i
        result = tmp
        return result

