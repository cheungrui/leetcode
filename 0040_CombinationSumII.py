#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-25 08:51:16
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

import os
"""
40. Combination Sum II
Medium

619

32

Favorite

Share
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        lenc = len(candidates)
        if lenc == 1:
            if target == candidates[0]:
                return [[target]]
        result = self.combinationSum2(candidates[0:-1], target)
        k, lastnum = 0, candidates[-1]
        for i in range(lenc-1, -1, -1):
            if candidates[i] == lastnum:
                k += 1
            else:
                break
        targetot = target - lastnum*k
        if targetot == 0:
            result.append([lastnum]*k)
            return result
        elif targetot < 0:
            return result
        else:
            resultot = self.combinationSum2(candidates[:lenc-k], targetot)
            for i in resultot:
                result.append(i+[lastnum]*k)
        return result
