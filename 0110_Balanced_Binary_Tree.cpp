#include<bits/stdc++.h>
#include<string>
using namespace std;
/*
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    //为了达到O（1）的算法复杂度加入了一个检测机制，当有子树不和要求的时候回传递上来
    int diffdepth(TreeNode* root){
        if(root==NULL){return 0;}
        int a=0,b=0;
        a=diffdepth(root->left);
        b=diffdepth(root->right);
        if(a==-1 || b==-1){return -1;}//有子树不合要求
        if(abs(a-b)>1){return -1;}//这个节点不合要求
        return (a>b)?(a+1):(b+1);//返回这个树的高
    }
    bool isBalanced(TreeNode* root) {
        if(root==NULL){return true;}
        int a=0;
        a=diffdepth(root);
        if(a==-1){return false;}
        return true;
        // a=diffdepth(root->left);//左子树
        // b=diffdepth(root->right);//右子树
        // if(a==-1 || b==-1){return false;}
        // if(abs(a-b)>1){return false;}//看差额
        // return true;
    }
};