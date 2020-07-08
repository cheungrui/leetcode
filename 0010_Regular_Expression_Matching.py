#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-30 13:53:55
# @Author  : Zhang Rui (1484659706@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def __init__(self):
		#记载不匹配的集合，元素是元组，(m,n)：表示s后m位和p后n位不匹配
		self.set_notmatch = set()
	def getLengthBeginSame(self, s, p):
		"""
		p是一个单字母，s是一个字符串
		求s开头有多少个重复的p
		"""
		length = 0
		for i in s:
			if i == p or p == ".":
				length += 1
			else:
				break
		return length

	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		len_s = len(s)
		len_p = len(p)

		if (len_s, len_p) in self.set_notmatch:
			return False

		if not p:
			if not s:
				return True
			self.set_notmatch.add((len_s, len_p))
			return False

		if p[0] == "*":
			return False

		if len_p == 1:
			if len_s == 1 and (p == "." or p == s):
				return True
			self.set_notmatch.add((len_s, len_p))
			return False

		if p[1] == "*":
			len_beginsame = self.getLengthBeginSame(s, p[0])
			for i in range(len_beginsame, -1, -1):
				if (len_s-i, len_p-2) in self.set_notmatch:
					continue
				if self.isMatch(s[i:], p[2:]):
					return True
				# self.set_notmatch.add((len_s - i, len_p - 2))
			self.set_notmatch.add((len_s, len_p))
			return False
			
		if len(s)>0 and (p[0] == s[0] or p[0] == "."):
			if (len_s-1, len_p-1) in self.set_notmatch:
				return False
			return self.isMatch(s[1:], p[1:])
		return False

if __name__ == "__main__":
	classa = Solution()
	# s = "aaaaabaccbbccababa"
	# p = "a*b*.*c*c*.*.*.*c"
	s = "abca"
	p = "a*ab*bc*ca*as*b*a"

	print(classa.isMatch(s, p))
	print(classa.set_notmatch)
	# print(classa.getLengthBeginSame("aba", p[1]))		
