#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-04 09:21:28
# @Author  : Zhang Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
33. Search in Rotated Sorted Array
Medium
1696
257


Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
"""
已知一个递增
初步的想法是1,先找到转折点，从而确定target所在的递增序列,logn复杂度;2,寻找符合的数字logn复杂度，

"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        m, n = 0, len(nums)-1
        while(m<=n):
            mid = (m+n)//2
            if nums[mid] == target:
                return mid
            #这个地方要注意界限的判断因为mid是可以=m的
            #前半段
            if nums[mid] >= nums[m]:
                #因为m-mid是递增的判断target是否处于该范围
                if target < nums[mid] and target >= nums[m]:
                    n = mid - 1
                else:
                    m = mid + 1
            #位于后半段
            else:
                #因为mid-n是递增的判断target是否处于该范围
                if target > nums[mid] and target <= nums[n]:
                    m = mid + 1
                else:
                    n = mid - 1
        return -1

if __name__ == "__main__":
    s = Solution()
    l = [4,5,6,7,0,1,2]
    m = 0
    print(s.search(l,m))




