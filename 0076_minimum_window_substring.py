#-*-coding:utf-8-*-
'''
这道题目的思路是这样的，首先确定要求的各个字母的数量
1一开始字符串的左右都在0这个位置，将右端不断的像右移动直到截取的字符串满足条件，这就是可行的结果之一，但是不够短
2再将左边的位置向右移动，直到找到可以满足条件的临界点，这样就是第一个满足条件的相对小的字符串，然后左边界再右移一下，这样结果就不满足了；
3重复1-2的过程，取最短的那个
4右边界超出，循环结束，到最后都没找到的话，那么结果就是空字符串

举个例子：
s="cabefgecdaecf",t="cae"
1,cabe满足条件
2，cabe，长度=4，左边界右移至abe
3，abefgec满足条件
4，abefgec相对最短，长度为7，左边界右移至befgec
5，befgecda满足条件
6，ecda相对最短，长度为4，左边界右移至cda
7，cdae满足条件
8，cdae相对最短，长度为4，左边界右移至dae
9.daec满足条件
10，aec相对最短，长度为3，左边界右移至ec
11，没有满足条件的了
'''
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        len_s = len(s)
        #print("len_s={}".format(len_s))
        len_t = len(t)
        #print("len_t={}".format(len_t))
        dic_t = {}
        result = ""
        count = 0
        minlen = len_s
        if len_t > len_s:
            return ""
        for i in t:
            if i not in dic_t:
                dic_t[i] = 1
            else:
                dic_t[i] += 1
        #print("dic_t=%s"% dic_t)
        l, r = 0, 0
        for r in range(len_s):
            if s[r] in dic_t:
                #dic_t表示各个字母需要多少个
                dic_t[s[r]] -= 1
                #说明这个字母是有用的字母
                #负数的话说明这个字母超标了
                #打个比方如果需要“a”这个字母2个，但是dic_t['a']==-1,那么说明已经有3个了
                if dic_t[s[r]]>=0:
                    count += 1
                    #print("11,l=%d,r=%d,count=%d"%(l, r, count))
            else:
                #这个字母不在字典里面，可以继续下一个字母了
                continue
            #需要的字母已经足够了，现在来缩减左边界
            while(count == len_t):
                if s[l] not in dic_t:
                    l += 1
                    continue
                dic_t[s[l]] +=1
                #小于等于0说明虽然这个元素是需要的，但是之前超标了
                if dic_t[s[l]] <= 0:
                    l += 1
                    continue
                print("%s,l=%d,r=%d"%(s[l:r+1],l,r))
                #这个元素是至关重要的元素有这个元素的话就是成立，否则不成立
                if (r+1-l) <= minlen:#这边之所以是<=是因为考虑到如果答案就是s整个字符串，那么就要加上=，而且题目也说了结果是唯一的
                    minlen = r+1-l
                    result = s[l:r+1]
                    #print("22 l=%d,r=%d,result=%s,count=%d,minlen=%d"%(l,r,result,count,minlen))
                count -= 1 
                l += 1
        return result

if __name__ == "__main__" :
	classa = Solution()
	print(classa.minWindow("cabefgecdaecf","cae"))