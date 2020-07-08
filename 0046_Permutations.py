#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-21 09:45:44
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

import os
"""
46. Permutations
Medium

1458

38

Favorite

Share
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # result = [[]]
        # for i, num in enumerate(nums):
        #     tmp = []
        #     for line in result:
        #         tmp.extend([line[:j]+[num]+line[j:] for j in range(i+1)])
        #     result = tmp
        # return result
        result = [[]]
        for i, num in enumerate(nums):
            result = [line[:j]+[num]+line[j:] for j in range(i+1) for line in result]
        return result