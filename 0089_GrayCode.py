#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-05 10:35:47
# @Author  : Zhang Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
89. Gray Code
Medium
267
919


The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
"""
"""
常试着写一下3位格雷码
0000,0001,0011,0010,
0110,0111,0101,0100,
可以看到
1、前2位和2位格雷码相同
2、后两位看到前半段和后半段是顺序相反的，
4位格林码也是如此
所以解决思路也就显而易见了，
"""
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        #0位格雷码
        result.append(0)
        for i in range(1, n+1):
            #num是前面的数字个数也是后面的数字要加的数
            num = 2**(i-1)
            #从后向前取反方向
            result.extend((i+num for i in reversed(result)))
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.grayCode(3))

