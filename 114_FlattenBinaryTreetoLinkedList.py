#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-11 18:37:27
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
"""
就是将二叉树按照深度优先的顺序进行遍历,变成一个每个节点都只有右儿子的树
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        node = root
        nodelist = []
        if node.right:
            nodelist.append(node.right)
        if node.left:
            nodelist.append(node.left)
        while nodelist:
            n = nodelist[-1]
            nodelist.pop()
            if n.right:
                nodelist.append(n.right)
            if n.left:
                nodelist.append(n.left)
            node.left = None
            node.right = n
            node = n





