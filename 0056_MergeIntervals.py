#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-12 13:00:29
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
56. Merge Intervals
Medium
1483
116
Favorite
Share
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals_len = len(intervals)
        if intervals_len < 2:
            return intervals
        intervals.sort(key=lambda i: i.start)
        result = []
        result.append(intervals[0])
        for i in range(1, intervals_len):
            tmp = intervals[i]
            if result[-1].end < tmp.start:
                result.append(tmp)
            else:
                result[-1].end = max(result[-1].end, tmp.end)
        return result
