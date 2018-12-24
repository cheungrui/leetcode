#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-18 17:46:31
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$
"""
65. Valid Number
Hard

323

2456

Favorite

Share
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
"""
"""
底数部分的开头符号位没有或者为1位,数字部分纯数字或者带小数点,有整数部分(整数部分不为空)小数点后可以无数字,没有整数部分小数点后必须有数字

e之后只能为整数
"""
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if re.match(r'\s*(\+|-)?((\d+\.?\d*)|(\.\d+))(e(\+|-)?(\d)+)?\s*$', s):
            return True
        return False
