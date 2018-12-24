#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-20 13:31:49
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        i, j, match_s, star_p = 0, 0, -1, -1
        while i < len(s):
            print(i, j, match_s, star_p)
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                match_s, star_p = i, j
                j += 1
            elif star_p >= 0:
                i, j = match_s + 1, star_p + 1
                match_s += 1
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)

if __name__ == "__main__":
    s = abacaba
    p = a*a*a