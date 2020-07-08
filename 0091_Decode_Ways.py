#-*-coding:utf-8-*-
class Solution:
    '''
    类似于斐波拉契数列
    可以用动态规划的方法求解
    这道题的问题在于2点：
    1、两位数在26以内
    2,0只能是第二位数字，所以是10或者20
    '''
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #如果第一个数字是0，没有合适的输出
        if s[0] == '0':
            return 0
        len_s = len(s)
        #这里为了动态规划的一致性，加了一个输入为""时，输出是1
        if len_s == 0 or len_s == 1:
            return 1
        #numset指的是字符串截取指定长度对应的输出数量，numset[0]指空字符串是输出数量是1，numset[1]=1单字符时输出数量是12
        numset = {}
        numset[0], numset[1] = 1, 1
        for i in range(2, len_s+1):
            #s[i-1]是指第i个字符
            #新输入一个0
            if s[i-1] == '0':
                #上一个输出是1或者2，最后两个必然凑成1队
                if s[i-2] in "12":
                    numset[i] = numset[i-2]
                else:
                    #30、00之类的不可能
                    return 0
            #最后的数字不是0，按照最后两个数能否组合分成两种情况
            else:
                tmp = int(s[i-2:i])
                if tmp>26 or tmp<11:
                    numset[i] = numset[i-1]
                else:
                    numset[i] = numset[i-2] + numset[i-1]
        return numset[len_s]