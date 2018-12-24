#include<bits/stdc++.h>
#include<string>
using namespace std;

class Solution {
public:
    //to add two num
    string add(string num1,string num2){
        int len1=num1.length(),len2=num2.length();
        int count=0,m1=len1-1,m2=len2-1,tmp=0;
        string sum="";
        while(m1>=0 && m2>=0){
            tmp=(num1[m1]-'0')+(num2[m2]-'0')+count;
            sum.push_back(tmp%10+'0');
            count=tmp/10;
            m1--;
            m2--;
        }
        while(m1>=0){
            tmp=(num1[m1]-'0')+count;
            sum.push_back(tmp%10+'0');
            count=tmp/10;
            m1--;
        }
        while(m2>=0){
            tmp=(num2[m2]-'0')+count;
            sum.push_back(tmp%10+'0');
            count=tmp/10;
            m2--;
        }
        if(count==1){
            sum.push_back('1');
        }
        reverse(sum.begin(),sum.end());
        return sum;
    }
    //when i know the first num.length =i,and the seconde num.length=j,then to know is the string right;
    //can also not use recursion;but i use tail recursion
    bool isAdditiveNumber2(string num,int i,int j){
        string sum="";
        int k=0;
        sum=add(num.substr(0,i),num.substr(i,j));
        k=sum.length();
        if(i+j+k>num.length()){
            return false;
        }
        if(sum==num.substr(i+j,k)){
            if(i+j+k==num.length()){return true;}
            return isAdditiveNumber2(num.substr(i,num.length()-i),j,k);
        }
        return false;
    }
    int min(int a,int b){
        return (a>b)?b:a;
    }
    bool isAdditiveNumber(string num) {
        int len_num=num.length(),L=(num.length()-1)/2;
        if(len_num<=2){return false;}//right or false,i don't know
        int i=1,j=1,maxj=1;
        if(num[0]=='0'){L=1;}
        for(i=1;i<L+1;i++){
            maxj=min(len_num-2*i,(len_num-i)/2);
            if(num[i]=='0'){maxj=1;}//the second num can only be 0
            for(j=1;j<maxj+1;j++){
                if(isAdditiveNumber2(num,i,j)){
                    return true;
                }
            }
        }
        return false;
    }
};

int main(){
    Solution s1;
    string s="422211115113515455115555555511211511221152121411152368429315214222111151135154551155555555112115112211521214111523703706563284442223022703091023111111102242302244230424282230473879997153126663334534054636534666666653363453366345636423345710917062785211105557556757727557777777755605755610576060705576184797059938337768892090812364092444444408969208976921697128921895714122723548874449647570091650222222164574964587497757834498080511182661886643341738382455742666666573544173564419454963419976225305384143551779138595254739288888873811913815191721279791805673648804523221611331243350031355555553116633117163366677613380329617934293757678924510287550528444444049782449868253880559256089698281474";
    string a="42221111511351545511555555551121151122115212141115236648797410",b="194134111";
    string tmp;
    
    // for(int i=0;i<11;i++){   
    //     tmp=s1.add(a,b);
    //     cout<<tmp<<"";
    //     a=b;
    //     b=tmp;
    // }
    //cout<<s1.isAdditiveNumber(s)<<endl;
    cout<<(-1>>1)<<endl;
    return 0;
}