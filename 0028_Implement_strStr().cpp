class Solution {
public:
    bool isMatch(string s, string p, int m, int n, int len){
        for(int i=0;i<len;i++){
            if(s[m+i] != p[n+i]){
                return false;
            }
        }
        return true;
    }
    int strStr(string haystack, string needle) {
        int len_hay = haystack.length();
        int len_needle = needle.length();
        if(0 == len_needle){
            return 0;
        }
        if(len_hay<len_needle){return -1;}
        for(int i=0;i<len_hay-len_needle+1;i++){
            if (isMatch(haystack,needle,i,0,len_needle)){
                return i;
            }
        }
        return -1;
    }
};
