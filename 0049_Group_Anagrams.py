#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-22 17:49:01
# @Author  : Zhang Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$
'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
class Solution:
    def getDictFromStrs(self, strs):
        """
        将字符串数组按照组成变为字典
        """
        dict_strs = {}
        for s in strs:
            a = tuple(sorted(s))
            if a not in dict_strs:
                dict_strs[a] = []
            dict_strs[a].append(s)
        return dict_strs

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_strs = self.getDictFromStrs(strs)
        return list(dict_strs.values())
