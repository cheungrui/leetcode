#include<bits/stdc++.h>
using namespace std;
/*
67. Add Binary
Easy
713
148


Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
*/
class Solution {
public:
    string addBinary(string a, string b) {
        string s;
        int a_len=a.length(), b_len=b.length();
        int i=a_len-1, j=b_len-1;
        int count=0,tmp=0;
        while(i>=0 and j>=0){
            tmp = (a[i]-'0') + (b[j]-'0') + count;
            if(tmp==0){
                s.push_back('0');
                count=0;
            }else if(tmp==1){
                s.push_back('1');
                count=0;
            }else if(tmp==2){
                s.push_back('0');
                count=1;
            }else{
                s.push_back('1');
                count=1;
            }
            i--;
            j--;
        }
        while(i>=0){
            tmp = (a[i]-'0') + count;
            if(tmp==0){
                s.push_back('0');
                count=0;
            }else if(tmp==1){
                s.push_back('1');
                count=0;
            }else{
                s.push_back('0');
                count=1;
            }
            i--;
        }
        while(j>=0){
            tmp = (b[j]-'0') + count;
            if(tmp==0){
                s.push_back('0');
                count=0;
            }else if(tmp==1){
                s.push_back('1');
                count=0;
            }else{
                s.push_back('0');
                count=1;
            }
            j--;
        }
        if(count){
            s.push_back('1');
        }
        reverse(s.begin(),s.end());
        return s;
    }
};

int main(){
    string a="1";
    string b="11";
    string s;
    s = addBinary(a,b);
    cout<<s<<endl;
    return 0;
}