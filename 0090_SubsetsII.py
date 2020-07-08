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
        if not nums:
            return result
        tmp, time = nums[0], 0
        for num in nums:
            if num == tmp:
                time += 1
            else:
                print(result, time, tmp)
                result.extend([i+[tmp]*j for j in range(1, time+1) for i in result])
                time, tmp = 1, num
        print(result, time, tmp)
        result.extend([i+[tmp]*j for j in range(1, time+1) for i in result])
        return result
