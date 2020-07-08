#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-03 23:53:05
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : http://www.cctv.com/
# @Version : $Id$

import os
"""
93. Restore IP Addresses
Medium
473
177


Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"] 
"""
"""
题目的大意是一个字符串分成4个数字，数字除了0以外不能以0位开口,大小在0-255中间，可以fen成多少种
动态规划即可
对于一个索引i，分成k分有l种分法，按照这样的方法来计算，就可以了
"""
class Solution:

    def isValidNum(self, s):
        """
        用来计算ip地址中间的某一个字符串是否合法
        """
        if not s.isdigit():
            return False
        if int(s) <= 255 and str(int(s)) == s:
            return True
        return False

    def getIndexValues(self, s, i, k, dict_kinds):
        """
        计算第i索引为结尾的字符串分成k个满足条件的数字的个数，并且加入到dict_kinds中
        """
        s_len = len(s)
        #长度不够
        if s_len < i+1:
            return
        #ip首位
        if k == 1:
            s1 = s[:i+1]
            if self.isValidNum(s1):
                dict_kinds[(i, k)] = [s1]
        else:
            # print(k)
            l2 = []
            #新加入的ip的长度
            for j in range(1, 4):
                l1 = dict_kinds.get((i-j, k-1), [])
                s1 = s[i-j+1 : i+1]
                if self.isValidNum(s1):
                    for s2 in l1:
                        s3 = ".".join([s2, s1])
                        l2.append(s3)
            if l2:
                dict_kinds[(i, k)] = l2

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s_len = len(s)
        dict_kinds = {}
        for i in range(s_len-1):
            for k in range(1, 4):
                self.getIndexValues(s, i, k, dict_kinds)
        self.getIndexValues(s, s_len-1, 4, dict_kinds)
        result = dict_kinds.get((s_len-1, 4), [])
        return result

