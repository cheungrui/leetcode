#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-09 10:25:12
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
