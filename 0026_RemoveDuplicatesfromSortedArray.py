#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-29 13:58:23
# @Author  : Zhang Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

import os
"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

"""
给定一个排序好的列表,去掉其中的重复项,空间复杂度要求O(1),返回的值是长度,对超过长度的部分不用管
"""
"""
设定两个索引,然后不断的将后面的不同的数字写到前一个索引中就可以了
"""
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m, n = 0, 0
        tmp = None
        while(n<len(nums)):
            if nums[n] == tmp:
                n +=1
                continue
            tmp= nums[n]
            nums[m] = tmp
            m += 1
            n += 1
        return m