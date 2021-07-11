/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */

// -----------------------------------------
// Model Solution: Multiset
//
// Time  Complexity: O(log(n))
// Space Complexity: O(n)
// -----------------------------------------
// n := nums.size()
//
// Ref: https://leetcode.com/problems/find-median-from-data-stream/discuss/1330697/C%2B%2B-Short-and-Clean-Solution-Using-One-Multiset-5-Lines-of-Code
class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {}

    void addNum(int num) {
        nums.insert(num);
        nums_size_even = !nums_size_even;

        // mid_iterator stays at nums.end() after first element inserted and ++mid_iterator moves mid_iterator to nums.begin()
        if (mid_iterator == nums.end() || (nums_size_even && *mid_iterator <= num))
            ++mid_iterator;
        if (!nums_size_even && *mid_iterator > num)
            --mid_iterator;
    }

    double findMedian() {
        return nums_size_even ? ((*mid_iterator + *prev(mid_iterator)) / 2.0) : *mid_iterator;
    }

private:
    multiset<int> nums;
    multiset<int>::iterator mid_iterator = nums.begin();
    bool nums_size_even = true;
};
