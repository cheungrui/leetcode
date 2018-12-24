#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-23 15:01:23
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
57. Insert Interval
Hard

631

79

Favorite

Share
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        if not intervals:
            return [newInterval]
        intervals_len = len(intervals)
        i = 0
        while(i<intervals_len and intervals[i].end < newInterval.start):
            result.append(intervals[i])
            i += 1
        while(i<intervals_len and intervals[i].end >= newInterval.start and intervals[i].start <= newInterval.end):
            newInterval.start = min(intervals[i].start, newInterval.start)
            newInterval.end = max(intervals[i].end, newInterval.end)
            i += 1
        result.append(newInterval)
        while(i<intervals_len):
            result.append(intervals[i])
            i += 1
        return result