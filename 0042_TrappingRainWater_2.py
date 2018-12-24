#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-11 13:45:57
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
42. Trapping Rain Water
Hard
2489
47
Favorite
Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height_len = len(height)
        if height_len < 3:
            return 0
        maxindex = height.index(max(height))
        sum = 0
        tmp = height[0]
        for i in range(1, maxindex):
            tmp = max(tmp, height[i])
            sum += tmp - height[i]
        tmp = height[height_len-1]
        for i in range(height_len-2, maxindex, -1):
            tmp = max(tmp, height[i])
            sum += tmp - height[i]
        return sum
