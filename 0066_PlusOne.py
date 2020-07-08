#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-03 09:31:53
# @Author  : Zhang Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

'''
66. Plus One
Easy
653
1204


Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
"""
递归即可easy
算法复杂度应该是O(n)
"""
class Solution:
    def plusOneatIndex(self, digits, i):
        """
        在指定index+1
        """
        if i < 0:
            digits.insert(0, 1)
        else:
            s = digits[i] + 1
            digits[i] = s % 10
            count = s // 10
            if count:
                self.plusOneatIndex(digits, i-1)
        return None

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dig_len = len(digits)
        self.plusOneatIndex(digits, dig_len - 1)
        return digits