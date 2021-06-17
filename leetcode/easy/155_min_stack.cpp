/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(1)
// Space Complexity: O(n)
// -----------------------------------------
// Ref: https://leetcode.com/problems/min-stack/discuss/49016/C%2B%2B-using-two-stacks-quite-short-and-easy-to-understand

class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {}
    
    void push(int val) {
        main_stack.push_back(val);
        if (min_stack.empty() || val <= min_stack.back())
            min_stack.push_back(val);
    }

    void pop() {
        int value_to_pop = main_stack.back();
        main_stack.pop_back();
        if (value_to_pop == min_stack.back())
            min_stack.pop_back();
    }

    int top() {
        return main_stack.back();
    }

    int getMin() {
        return min_stack.back();
    }

private:
    vector<int> main_stack;
    vector<int> min_stack;
};
