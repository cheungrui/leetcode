#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-10 17:00:18
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

import os
"""
79. Word Search
Medium

Share
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
class Solution(object):
    def searchWordinBoard(self, board, word, len_word, n, i, j, pathset):
        """
        :type board:list[list[str]]
        :type word:str
        :type n,i,j:int
        :type pathset:set
        :rtype:bool
        几个参数分别代表矩阵,单词,单词长度,当前字母,当前矩阵位置,已经经过的路径集合
        """
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
            return False
        if word[n]!=board[i][j] or (i,j) in pathset:
            return False
        if n == len_word-1:
            return True
        pathset.add((i,j))
        result = self.searchWordinBoard(board, word, len_word, n+1, i-1, j, pathset) or \
            self.searchWordinBoard(board, word, len_word, n+1, i, j-1, pathset) or \
            self.searchWordinBoard(board, word, len_word, n+1, i+1, j, pathset) or \
            self.searchWordinBoard(board, word, len_word, n+1, i, j+1, pathset)
        pathset.remove((i,j))
        return result


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == "":
            return True
        if not board or not board[0]:
            return False
        len_row, len_col = len(board), len(board[0])
        for i in range(len_row):
            for j in range(len_col):
                if word[0] != board[i][j]:
                    continue
                if self.searchWordinBoard(board, word, len(word), 0, i, j, set()):
                    return True
        return False

if __name__ == "__main__":
    S = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(S.exist(board, word))