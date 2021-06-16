/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */

// -----------------------------------------
// My Solution
//
// Space Complexity: O(n)
// -----------------------------------------
// n := numbers received total
#include <queue>

class MyStack {
public:
    /** Initialize your data structure here. */
    MyStack() {}

    /** Push element x onto stack. */
    // Time Complexity: O(n)
    void push(int x) {
        nums_queue.push(x);
        if (nums_queue.size() > 1) {
            for (int index = 1; index < nums_queue.size(); ++index) {
                nums_queue.push(nums_queue.front());
                nums_queue.pop();
            }
        }
    }

    /** Removes the element on top of the stack and returns that element. */
    // Time Complexity: O(1)
    int pop() {
        int top_element = nums_queue.front();
        nums_queue.pop();
        return top_element;
    }

    /** Get the top element. */
    // Time Complexity: O(1)
    int top() {
        return nums_queue.front();
    }

    /** Returns whether the stack is empty. */
    // Time Complexity: O(1)
    bool empty() {
        return nums_queue.size() == 0;
    }

private:
    queue<int> nums_queue;
};
