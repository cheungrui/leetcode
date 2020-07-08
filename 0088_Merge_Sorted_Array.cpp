// Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

// Note:

// The number of elements initialized in nums1 and nums2 are m and n respectively.
// You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
// Example:

// Input:
// nums1 = [1,2,3,0,0,0], m = 3
// nums2 = [2,5,6],       n = 3

// Output: [1,2,2,3,5,6]

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        stack<int> stack1;
        while(nums1.size()>m){
            nums1.pop_back();
        }
        while(nums2.size()>n){
            nums2.pop_back();
        }
        while(!nums1.empty() && !nums2.empty()){
            m = nums1.back();
            n = nums2.back();
            if(m>n){
                stack1.push(m);
                nums1.pop_back();
            }else{
                stack1.push(n);
                nums2.pop_back();
            }
        }
        while(!nums2.empty()){
            stack1.push(nums2.back());
            nums2.pop_back();
        }
        while(!stack1.empty()){
            nums1.push_back(stack1.top());
            stack1.pop();
        }
    }
};