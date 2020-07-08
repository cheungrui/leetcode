"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []
"""

"""
一个字符串s,一个字符串的数组，数组中字符串的长度是相等的，
求所有可能的索引，以这个索引为开头的s的子串恰好为数组中字符串的组合
"""

"""
我想起来同样是leetcode的某道题目，题号记不得了，不过那道题目的子串列表变为了一个相对较短的字符串
首先将单个word的长度记做word_len,words中单词的个数记做是words_len
也就是可以这样想,将s分割成一段一段的,每一段都是word_len的长度,这样总共有word_len种可能,我们对这些可能分别讨论
不记顺序肯定是要用字典的,
创建一个字典来记载words中的单词分布也就是各个单词的个数,同时对前words_len的段数同样也做单词分布的统计,如果两相符合就ok,
接下来每加入一个单词就同时删去开头的单词的统计,再比较,一次类推就能做出来
"""
class Solution:
    def isVaildWords(self, words):
        """
        检测words中的元素长度是否一致
        """

        if not words:
            return True
        word_len = len(words[0])
        for word in words:
            tmp_len = len(word)
            if tmp_len != word_len:
                return False
        return True

    def addWordToDic(self, word, dic_words):
        if word in dic_words:
            dic_words[word] += 1
        else:
            dic_words[word] = 1

    def subWordToDic(self, word, dic_words):
        if word in dic_words:
            dic_words[word] -= 1
        else:
            dic_words[word] = -1

    def getDictFromWords(self, words):
        """
        将words中的单词情况统计到字典中去,并取负数,也就是要填充的单词的个数
        """
        dic_words = {}
        for word in words:
            self.subWordToDic(word, dic_words)
        return dic_words

    def checkDictZone(self, dic_words):
        """
        检测字典的values是不是都是0
        """
        for key in dic_words:
            if dic_words[key] != 0:
                return False
        return True

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        s_len = len(s)
        #s是空字符串时候的处理
        if not s_len:
            return []
        #判断words是否有效
        if not self.isVaildWords(words):
            return []
        #words为空
        if not words:
            return []
        words_len = len(words)
        word_len = len(words[0])
        str_len = words_len * word_len
        result = []
        #将可能的情况根据index被单个单词长度整除的情况分组
        for startindex in range(word_len):
            # #s长度压根就不够的情况,此时长度不够以后长度都会不够
            if s_len < words_len * word_len - startindex:
                break
            # 这边获得要填充的words的字典情况
            dic_words = self.getDictFromWords(words)
            index = startindex
            #先把指定长度的word都放进去
            for i in range(words_len):
                #放单词
                tmpword = s[index + word_len*i: index + word_len*(i+1)]
                self.addWordToDic(tmpword, dic_words)
            #检测是否正确
            if self.checkDictZone(dic_words):
                result.append(index)
            #判断长度后面还有没有单词段了
            while(index + word_len + str_len <= s_len):
                #去掉首单词
                tmpword = s[index : index + word_len]
                self.subWordToDic(tmpword, dic_words)
                #增加尾单词
                tmpword = s[index + str_len : index + str_len + word_len]
                index += word_len
                self.addWordToDic(tmpword, dic_words)
                #判断正确性
                if self.checkDictZone(dic_words):
                    result.append(index)
        #调整顺序
        result.sort()
        return result






        