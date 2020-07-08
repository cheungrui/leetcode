#include<bits/stdc++.h>
#include<string>
using namespace std;
/*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
*/
class MinStack {
public:
    stack<int> stack_1;
    stack<int> stack_2;
    /** initialize your data structure here. */
//     MinStack() {
        
//     }
    
    void push(int x) {
        if(stack_2.empty() || getMin()>x){
            stack_1.push(x);
            stack_2.push(x);
        }else{
            stack_1.push(x);
            stack_2.push(stack_2.top());
        }
    }
    
    void pop() {
        stack_1.pop();
        stack_2.pop();
    }
    
    int top() {
        return stack_1.top();
    }
    
    int getMin() {
        return stack_2.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */