// -----------------------------------------
// My Solution
//
// Time  Complexity: O(mn)
// Space Complexity: O(mn)
// -----------------------------------------
// m := grid[0].size(), n := grid.size()
class Solution {
public:
    int largestIsland(vector<vector<int>>& grid) {
        grid_side_length = grid.size();
        cell_visited = vector<vector<bool>>(grid_side_length, vector<bool>(grid_side_length, false));
        cell_group_index = vector<vector<int>>(grid_side_length, vector<int>(grid_side_length));

        int curr_group_index = 1;
        int max_island_size  = 0;
        for (int row = 0; row < grid_side_length; ++row) {
            for (int col = 0; col < grid_side_length; ++col) {
                if (grid[row][col] == 1 && !cell_visited[row][col]) {
                    int island_size = 0;
                    calc_island_size(grid, row, col, island_size);
                    if (island_size == 1)
                        cell_group_index[row][col] = curr_group_index;
                    else
                        fill_island_size_group(grid, row, col, island_size, curr_group_index);
                    ++curr_group_index;

                    max_island_size = max(max_island_size, island_size);
                }
            }
        }

        unordered_set<int> visited_groups;
        for (int row = 0; row < grid_side_length; ++row) {
            for (int col = 0; col < grid_side_length; ++col) {
                if (grid[row][col] == 0) {
                    visited_groups.clear();

                    int island_size = 1;
                    for (int index = 0; index < next_cell_movement.size(); ++index) {
                        int next_row = row + next_cell_movement[index].first;
                        int next_col = col + next_cell_movement[index].second;
                        if (position_valid(next_row, next_col))
                            continue;

                        int group_index = cell_group_index[next_row][next_col];
                        if (visited_groups.find(group_index) == visited_groups.end()) {
                            island_size += grid[next_row][next_col];
                            visited_groups.insert(group_index);
                        }
                    }

                    max_island_size = max(max_island_size, island_size);
                }
            }
        }

        return max_island_size;
    }

private:
    int grid_side_length;
    vector<vector<bool>> cell_visited;
    vector<vector<int>> cell_group_index;
    vector<pair<int, int>> next_cell_movement = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

    inline bool position_valid(int row, int col) {
        return row >= 0 && row < grid_side_length && col >= 0 && col < grid_side_length;
    }

    void calc_island_size(vector<vector<int>>& grid, int row, int col, int& island_size) {
        if (!position_valid(row, col))
            return;

        if (grid[row][col] == 1 && !cell_visited[row][col]) {
            cell_visited[row][col] = true;
            island_size += 1;

            calc_island_size(grid, row - 1, col, island_size);
            calc_island_size(grid, row + 1, col, island_size);
            calc_island_size(grid, row, col - 1, island_size);
            calc_island_size(grid, row, col + 1, island_size);
        }
    };

    void fill_island_size_group(vector<vector<int>>& grid, int row, int col, int island_size, int group_index) {
        if (!position_valid(row, col))
            return;

        if (grid[row][col] == 1 && grid[row][col] != island_size) {
            grid[row][col] = island_size;
            cell_group_index[row][col] = group_index;

            fill_island_size_group(grid, row - 1, col, island_size, group_index);
            fill_island_size_group(grid, row + 1, col, island_size, group_index);
            fill_island_size_group(grid, row, col - 1, island_size, group_index);
            fill_island_size_group(grid, row, col + 1, island_size, group_index);
        }
    }
};

// -----------------------------------------
// Model Solution: Union Find
//
// Time  Complexity: O(mn)
// Space Complexity: O(mn)
// -----------------------------------------
// m := grid[0].size(), n := grid.size()
//
// Ref: https://leetcode.com/problems/making-a-large-island/discuss/324287/union-find-c%2B%2B
class Solution {
public:
    int largestIsland(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();

        max_count = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[i].size(); ++j) {
                if (grid[i][j] == 1) {
                    int id = get_id(i, j);
                    parent[id] = id;
                    counter[id] = 1;
                    max_count = 1;
                }
            }
        }

        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[i].size(); ++j) {
                if (grid[i][j] == 1) {
                    int cell_id = get_id(i, j);
                    for (int k = 0; k < 4; ++k) {
                        int x = move[k][0] + i;
                        int y = move[k][1] + j;
                        if (x < 0 || y < 0 || x >= m || y >= n || grid[x][y] == 0)
                            continue;
                        union_set(cell_id, get_id(x, y));
                    }
                }
            }
        }

        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[i].size(); ++j) {
                if (grid[i][j] == 0) {
                    int count = 1;

                    unordered_set<int> prev_ids;
                    for (int k = 0; k < 4; ++k) {
                        int x = move[k][0] + i;
                        int y = move[k][1] + j;
                        if (x < 0 || y < 0 || x >= m || y >= n || grid[x][y] == 0)
                            continue;

                        int p_2 = find_parent(get_id(x, y));
                        if (prev_ids.find(p_2) == prev_ids.end()) {
                            prev_ids.insert(p_2);
                            count += counter[p_2];
                        }
                    }
                    max_count = max(count, max_count);
                }
            }
        }

        return max_count;
    }

private:
    int move[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int m;
    int n;
    int max_count;
    unordered_map<int, int> counter;
    unordered_map<int, int> parent;

    int get_id(int x, int y) {
        return x * n + y;
    }

    int find_parent(int x) {
        if (x != parent[x]) {
            return parent[x] = find_parent(parent[x]);
        }
        return parent[x];
    }

    void union_set(int x, int y) {
        int parent_1 = find_parent(x);
        int parent_2 = find_parent(y);

        if (parent_1 != parent_2) {
            int count_1 = counter[parent_1];
            int count_2 = counter[parent_2];
            if (count_1 > count_2) {
                parent[parent_2] = parent_1;
                counter[parent_1] += count_2;
                max_count = max(counter[parent_1], max_count);
            } else {
                parent[parent_1] = parent_2;
                counter[parent_2] += count_1;
                max_count = max(counter[parent_1], max_count);
            }
        }
    }
};
