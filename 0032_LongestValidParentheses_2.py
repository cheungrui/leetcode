#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-07 15:32:50
# @Author  : Zhang Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
32. Longest Valid Parentheses
Hard
1343
68


Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        maxlen = 0
        tmp = 0
        preleft = 0
        lastright = 0
        s = list(s)
        for i in range(s_len):
            if s[i] == "(":
                preleft += 1
            else:
                if preleft:
                    preleft -= 1
                else:
                    s[i] = "@"
                    preleft = 0
        # for i in range(s_len-1,-1,-1):
        #     if s[i] == ")" or s[i] == "@" :
        #         lastright += 1
        #     else:
        #         if lastright:
        #             lastright -= 1
        #         else:
        #             s[i] = "@"
        #             lastright = 0
        for i in range(s_len-1,-1,-1):
            if s[i] == ")":
                lastright += 1
            elif(s[i]=="@"):
                lastright = 0
            else:
                if lastright:
                    lastright -= 1
                else:
                    s[i] = "@"
                    lastright = 0
        for i in range(s_len):
            if s[i] != "@":
                tmp += 1
            else:
                maxlen = max(maxlen, tmp)
                tmp = 0
        return max(maxlen, tmp)
if __name__ == "__main__":
    s = ")()())()()("
    sol = Solution()
    print(sol.longestValidParentheses(s))



