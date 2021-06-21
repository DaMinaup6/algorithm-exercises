// -----------------------------------------
// My Solution
//
// Time  Complexity: O(n^3)
// Space Complexity: O(n^2)
// -----------------------------------------
// n := grid.size() == grid[0].size()
#include <set>

class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        this->grid = grid;
        this->size = grid.size();

        // e.g. grid == [[3, 2], [0, 1]], can only start when curr depth >= grid[0][0]
        for (int time = grid[0][0]; time <= pow(this->size, 2) - 1; ++time) {
            this->visited_points = set<pair<int, int>>();
            if (reach_target_point({0, 0}, time))
                return time;
        }
        return -1;
    }

    // cannot use pair<int, int>& for curr_point since {row, col} is non-constant lvalue
    // error message: `non-const lvalue reference to type 'pair<int, int>' cannot bind to an initializer list temporary`
    bool reach_target_point(pair<int, int> curr_point, int& curr_depth) {
        int row = curr_point.first, col = curr_point.second;

        if (row == this->size - 1 && col == this->size - 1)
            return true;
        if (this->visited_points.find(curr_point) != this->visited_points.end())
            return false;
        // make sure add curr_point to before visiting next_points
        this->visited_points.insert(curr_point);

        if (row - 1 >= 0 && this->grid[row - 1][col] <= curr_depth && reach_target_point({row - 1, col}, curr_depth))
            return true;
        if (col - 1 >= 0 && this->grid[row][col - 1] <= curr_depth && reach_target_point({row, col - 1}, curr_depth))
            return true;
        if (row + 1 < this->size && this->grid[row + 1][col] <= curr_depth && reach_target_point({row + 1, col}, curr_depth))
            return true;
        if (col + 1 < this->size && this->grid[row][col + 1] <= curr_depth && reach_target_point({row, col + 1}, curr_depth))
            return true;
        return false;
    }

private:
    vector<vector<int>> grid;
    set<pair<int, int>> visited_points; // cannot use unordered_set with pair so use set
    int size;
};

// -----------------------------------------
// Model Solution: Min Heap
//
// Time  Complexity: O(n^2 * log(n))
// Space Complexity: O(n^2)
// -----------------------------------------
// n := grid.size() == grid[0].size()

// -----> Version 1
// Ref: https://www.youtube.com/watch?v=amvrKlMLuGY
#include <queue>
#include <set>

class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int grid_size = grid.size();
        vector<pair<int, int>> point_moves = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

        min_heap.push({grid[0][0], 0, 0});
        visited_points.insert({0, 0});
        while (!min_heap.empty()) {
            tuple<int, int, int> curr_info = min_heap.top();
            min_heap.pop();

            int curr_max_depth = get<0>(curr_info);
            int row = get<1>(curr_info);
            int col = get<2>(curr_info);
            if (row == grid_size - 1 && col == grid_size - 1)
                return curr_max_depth;

            for (int index = 0; index < point_moves.size(); ++index) {
                int next_row = row + point_moves[index].first;
                int next_col = col + point_moves[index].second;
                if (next_row < 0 || next_row >= grid_size || next_col < 0 || next_col >= grid_size || visited_points.find({next_row, next_col}) != visited_points.end())
                    continue;

                visited_points.insert({next_row, next_col});
                min_heap.push({max(curr_max_depth, grid[next_row][next_col]), next_row, next_col});
            }
        }
        return -1;
    }

private:
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> min_heap;
    set<pair<int, int>> visited_points;
};

// -----> Version 2
// Ref: https://leetcode.com/problems/swim-in-rising-water/discuss/113770/C%2B%2BPython-PriorityQueue
#include <queue>

class Solution {
public:
    struct CellInfo {
        int max_depth, row, col;
        CellInfo(int depth, int row_index, int col_index) : max_depth(depth), row(row_index), col(col_index) {}
        // The reference is a reference to const, so it won't be possible to invoke member functions of CellInfo
        // Ref: https://stackoverflow.com/a/15999152
        bool operator< (const CellInfo &cell_info) const { return max_depth > cell_info.max_depth; }
    };

    int swimInWater(vector<vector<int>>& grid) {
        static int point_moves[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        int grid_size = grid.size();
        vector<vector<int>> visited_points(grid_size, vector<int>(grid_size, 0));

        // Initialize cell_info_priority_queue and visited_points
        cell_info_priority_queue.push(CellInfo(grid[0][0], 0, 0));
        visited_points[0][0] = 1;

        while (!cell_info_priority_queue.empty()) {
            CellInfo cell_info = cell_info_priority_queue.top();
            cell_info_priority_queue.pop();

            if (cell_info.row == grid_size - 1 && cell_info.col == grid_size - 1)
                return cell_info.max_depth;

            for (auto& move : point_moves) {
                int next_row = cell_info.row + move[0];
                int next_col = cell_info.col + move[1];
                if (0 <= next_row && next_row < grid_size && 0 <= next_col && next_col < grid_size && visited_points[next_row][next_col] == 0) {
                    visited_points[next_row][next_col] = 1;
                    cell_info_priority_queue.push(CellInfo(max(cell_info.max_depth, grid[next_row][next_col]), next_row, next_col));
                }
            }
        }
        return -1;
    }

private:
    priority_queue<CellInfo> cell_info_priority_queue;
};
