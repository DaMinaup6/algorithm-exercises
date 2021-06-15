// -----------------------------------------
// Model Solution
//
// Time  Complexity: O(n^2 * log(n))
// Space Complexity: O(n^2)
// -----------------------------------------
// n := points.size()
// Ref: https://www.youtube.com/watch?v=f7JOBJIC-NA
#include <cstdlib> // abs
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        // Adjacency List
        unordered_map<int, vector<pair<int, int>>> adjacency_list;
        for (int curr_point_index = 0; curr_point_index < points.size(); ++curr_point_index) {
            vector<int> curr_point = points[curr_point_index];

            for (int next_point_index = curr_point_index + 1; next_point_index < points.size(); ++next_point_index) {
                vector<int> next_point = points[next_point_index];

                int distance = abs(curr_point[0] - next_point[0]) + abs(curr_point[1] - next_point[1]);
                adjacency_list[curr_point_index].push_back({ distance, next_point_index });
                adjacency_list[next_point_index].push_back({ distance, curr_point_index });
            }
        }

        // Prim's Algorithm
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> cost_node_pair_min_heap;
        unordered_set<int> visited_nodes;
        int connection_cost = 0;

        cost_node_pair_min_heap.push({ 0, 0 });
        while (visited_nodes.size() < points.size()) {
            pair<int, int> curr_cost_node_pair = cost_node_pair_min_heap.top();
            int curr_cost = curr_cost_node_pair.first;
            int curr_node = curr_cost_node_pair.second;
            cost_node_pair_min_heap.pop();
            if (visited_nodes.find(curr_node) != visited_nodes.end())
                continue;

            visited_nodes.insert(curr_node);
            connection_cost += curr_cost;

            vector<pair<int, int>> neighbors = adjacency_list[curr_node];
            for (int index = 0; index < neighbors.size(); ++index) {
                pair<int, int> neighbor_cost_node_pair = neighbors[index];
                int neighbor_node = neighbor_cost_node_pair.second;
                if (visited_nodes.find(neighbor_node) == visited_nodes.end())
                    cost_node_pair_min_heap.push(neighbor_cost_node_pair);
            }
        }
        return connection_cost;
    }
};
