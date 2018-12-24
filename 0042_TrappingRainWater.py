#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-11 13:24:57
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
        if not height:
            return 0
        maxindex = height.index(max(height))
        dict_height = {-1:0, len(height):0}
        for i in range(maxindex+1):
            dict_height[i] = max(dict_height[i-1], height[i])
        for i in range(len(height)-1, maxindex, -1):
            dict_height[i] = max(dict_height[i+1], height[i])
        sum = 0
        for i in range(len(height)+1):
            sum += dict_height[i] - height[i]
        return sum
