// Implement pow(x, n), which calculates x raised to the power n (xn).

// Example 1:

// Input: 2.00000, 10
// Output: 1024.00000
// Example 2:

// Input: 2.10000, 3
// Output: 9.26100
// Example 3:

// Input: 2.00000, -2
// Output: 0.25000
// Explanation: 2-2 = 1/22 = 1/4 = 0.25
// Note:

// -100.0 < x < 100.0
// n is a 32-bit signed integer, within the range [−231, 231 − 1]

class Solution {
public:
    double myPow(double x, int n) {
        long long m=n;
        if(n<0){return pow(1/x, 0-m);}
        return pow(x, n);
    }
    double pow(double x, long long n) {
        if(0==n){return 1.0;}
        double a=0.0;
        a = pow(x, n/2);
        // cout<<a<<"   "<<n<<endl;
        if(n%2){
            return a*a*x;
        }else{
            return a*a;
        }
    }
};