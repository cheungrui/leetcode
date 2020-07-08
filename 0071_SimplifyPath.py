#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-26 21:34:23
# @Author  : Cheung Rui (1484659706@qq.com)
# @Link    : https://www.cnblogs.com/mangmangbiluo/
# @Version : $Id$

"""
71. Simplify Path
Medium

319

964

Favorite

Share
Given an absolute path for a file (Unix-style), simplify it. 

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a simplified path. Additionally, a double period ("..") moves up a directory, so it cancels out whatever the last directory was. For more information, look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""
"""
有路径就进栈,有..就出栈,.就跳过
"""
class Solution:
    def pushDir(self, pathlist, dirname):
        """
        将dirname加入路径列表中
        """
        if dirname == "" or dirname==".":
            pass
        elif dirname == "..":
            if pathlist:
                pathlist.pop()
        else:
            pathlist.append(dirname)

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathlist = []
        dirname = ""
        for i in path:
            if i != "/":
                dirname += i
            else:
                self.pushDir(pathlist, dirname)
                dirname = ""
        self.pushDir(pathlist, dirname)
        return "/"+"/".join(pathlist)