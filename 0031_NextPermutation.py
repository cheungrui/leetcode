#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-30 09:05:19
# @Author  : Zhang Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
"""
实现下一个排序，使得数字成为字典中的下一个更大的数字，
如果不可能，就让其排序为尽可能小
空间复杂度为O(1)
"""
"""
按照题意是要找打比原数大的尽可能小的数字，所以前面的数字要尽可能的不变，
可以这样分析，首先看最后两个数字，如果前一个比后一个大的话互换位置即可，
如果不行，就分析后三个，此时后两个数是有序的：前面的数要大于等于后面的数；在这两个数中，找到比第一个数字大的最小的那个数字，互换位置，再将后两个数重新排序
如果找不到，就分析后四个,依次类推
"""
class Solution:
    def swapmn(self, nums, m, n):
        nums[m], nums[n] = nums[n], nums[m]

    def findPreindex(self, nums, lastindex):
        """
        从lastindex开始从后向前应该是升序排列，找打打破规则的那个数的索引，返回-1说明整个列表都是降序
        """
        index = lastindex - 1
        while index >= 0:
            if nums[index] < nums[index + 1]:
                return index
            index -= 1
        return index

    def findChangeindex(self, nums, num, m, n):
        """
        找到降序数组nums[m:n+1]中，比num大的最小的数的索引，已知这个数必定存在
        """
        while(m < n):
            mid = (m + n + 1)//2
            if nums[mid] <= num:
                n = mid - 1
            else:
                m = mid
        return m

    def reversemn(self, nums, m, n):
        """
        对nums[m:n+1]进行倒序
        """
        while(m<n):
            self.swapmn(nums, m, n)
            m += 1
            n -= 1
        return

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        if nums_len < 2:
            return None
        preindex = self.findPreindex(nums, nums_len-1)
        #整个数组都是降序
        if preindex < 0:
            self.reversemn(nums, preindex+1, nums_len-1)
        else:
            #从后面的降序的列表中找到比preindex数字大的最小的数字索引
            changeindex = self.findChangeindex(nums, nums[preindex], preindex+1, nums_len-1)
            #互换，互换以后后面的数组依然是降序排列的
            self.swapmn(nums, preindex, changeindex)
            self.reversemn(nums, preindex+1, nums_len-1)
        return None
