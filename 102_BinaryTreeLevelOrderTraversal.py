#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-13 16:08:57
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
102. Binary Tree Level Order Traversal
Medium

1355

31

Favorite

Share
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
"""
给定一个二叉树,返回其结点的层次遍历
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        nodelist = [root]
        result = []
        while nodelist:
            tmplist = []
            vallist = []
            for node in nodelist:
                vallist.append(node.val)
                if node.left:
                    tmplist.append(node.left)
                if node.right:
                    tmplist.append(node.right)
            result.append(vallist)
            nodelist = tmplist
        return result