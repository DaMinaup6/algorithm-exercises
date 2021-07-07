// -----------------------------------------
// My Solution: Heap
//
// Time  Complexity: O(mn)
// Space Complexity: O(k)
// -----------------------------------------
// m := matrix.size(), n := matrix[0].size()
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue<int> max_heap;
        for (int row = 0; row < matrix.size(); ++row) {
            for (int col = 0; col < matrix[0].size(); ++col) {
                max_heap.push(matrix[row][col]);
                if (max_heap.size() > k)
                    max_heap.pop();
            }
        }

        return max_heap.top();
    }
};

// -----------------------------------------
// Model Solution: Binary Search
//
// Time  Complexity: O((m + n) * log(k))
// Space Complexity: O(1)
// -----------------------------------------
// m := matrix.size(), n := matrix[0].size()
//
// Ref: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1322101/C%2B%2BPython-Binary-Search-Picture-Explain-Clean-and-Concise
class Solution {
public:
    int m, n;

    int kthSmallest(vector<vector<int>>& matrix, int k) {
        m = matrix.size(), n = matrix[0].size(); // For general, the matrix need not be a square
        int left = matrix[0][0], right = matrix[m-1][n-1], ans = -1;
        while (left <= right) {
            int mid = (left + right) >> 1;
            if (count_less_or_equal(matrix, mid) >= k) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }

    int count_less_or_equal(vector<vector<int>>& matrix, int x) {
        int cnt = 0, c = n - 1; // start with the rightmost column
        for (int r = 0; r < m; ++r) {
            while (c >= 0 && matrix[r][c] > x)
                --c;  // decrease column until matrix[r][c] <= x
            cnt += (c + 1);
        }
        return cnt;
    }
};
