#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-24 19:09:55
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
60. Permutation Sequence
Medium

621

170

Favorite

Share
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if not n:
            return ""
        result = ""
        nums = [i for i in range(1, n+1)]
        numsfactorial = [1]
        for i in range(1, n):
            numsfactorial.append(numsfactorial[-1]*i)
        for i in range(n, 0, -1):
            j = (k-1)//numsfactorial[i-1]
            k = (k-1)%numsfactorial[i-1] + 1
            result += str(nums[j])
            del nums[j]
        return result
