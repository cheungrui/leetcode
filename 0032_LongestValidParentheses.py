#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-06 17:13:57
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
        preleftlist = []
        preleft = 0
        maxlen = 0
        tmp = 0
        tmplist = []
        i = 0
        while i < s_len:
            while i < s_len and s[i] == "(":
                preleft += 1
                i += 1
            if preleft:
                preleftlist.append(preleft)
                preleft = 0
            while i < s_len and s[i] == ")":
                if preleftlist:
                    tmp += 2
                    preleftlist[-1] -= 1
                    #这一层的左括号已经用完了
                    if not preleftlist[-1]:
                        preleftlist.pop()
                        #如果前面成对的()就把数量合并
                        if tmplist:
                            tmp += tmplist[-1]
                            tmplist.pop()
                #这个else说明右括号已经找不到可以匹配的左括号了
                else:
                    maxlen = max(tmp, maxlen)
                    tmp = 0
                    tmplist = []
                i +=1
            #之前的循环中右括号找到的tmp计算进去
            if tmp:
                tmplist.append(tmp)
                maxlen = max(tmp, maxlen)
            tmp = 0
        return max(tmp, maxlen)

if __name__ == "__main__":
    s = ")()())()()("
    sol = Solution()
    print(sol.longestValidParentheses(s))
