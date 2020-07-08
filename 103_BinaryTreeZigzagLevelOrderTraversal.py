#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-13 17:17:30
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

import os
"""
103. Binary Tree Zigzag Level Order Traversal
Medium

884

57

Favorite

Share
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
"""
在103题基础上添加一个翻转指示器之类的东西即可
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        nodelist = [root]
        result = []
        order = True
        while nodelist:
            tmplist = []
            vallist = []
            for node in nodelist:
                vallist.append(node.val)
                if node.left:
                    tmplist.append(node.left)
                if node.right:
                    tmplist.append(node.right)
            if not order:
                vallist.reverse()
            order = not order
            result.append(vallist)
            nodelist = tmplist
        return result
