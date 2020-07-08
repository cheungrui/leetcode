#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-22 13:42:36
# @Author  : Zhang Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""
"""
给定一个非负整数数组，你一开始在数组的开头，每个元素标表明了你在这一个点可以跳到的长度最大值，
判断能否到达终点
"""
"""
首先我们要想到的就是如果可以跳到a处，那么a之前的所有点都可以跳到
"""
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i in range(len(nums)):
            if i > reach:#i点是否可以到达
                return False
            reach = max(reach, i + nums[i])
        return True
        