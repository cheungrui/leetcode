#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-20 10:41:00
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
44. Wildcard Matching
Hard

796

58

Favorite

Share
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""
"""
依旧是匹配不过是linux系统下的匹配规则？匹配任意单一字符*匹配任意长度的字符（包括空）
用动态规划依旧可行s为原字符串，p为匹配字符串，（m,n)表示s的前m和p的前n位是否匹配
"""
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # dict_mn = {}
        # m = len(s)
        # n = len(p)
        # dict_mn[(0,0)] = True
        # for i in range(1, m+1):
        #     dict_mn[(i, 0)] = False
        # for j in range(1, n+1):
        #     # for i in range(0, m):
        #     pj = p[j-1]
        #     if pj == "?":
        #         for i in range(0, m+1):
        #             dict_mn[(i, j)] = dict_mn.get((i-1, j-1), False)
        #     elif pj == "*":
        #         for i in range(0, m+1):
        #             dict_mn[(i, j)] = dict_mn[(i, j-1)] or dict_mn.get((i-1, j), False)
        #     else:
        #         for i in range(0, m+1):
        #             dict_mn[(i, j)] = dict_mn.get((i-1, j-1), False) and s[i-1] == p[j-1]

        # return dict_mn[(m, n)]

        m = len(s)
        n = len(p)
        dp = [[None for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = False
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and p[j-1] == "*"
        for j in range(1, n+1):
            for i in range(1, m+1):
                pj = p[j-1]
                if pj == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif pj == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        return dp[m][n]