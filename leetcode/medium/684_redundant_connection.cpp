// -----------------------------------------
// Model Solution: Union Find
//
// Time  Complexity: O(nlog(n))
// Space Complexity: O(n)
// -----------------------------------------
// n := edges.size()
// Ref: https://www.youtube.com/watch?v=FXWRE67PLL0
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        node_parents.resize(edges.size() + 1);
        iota(node_parents.begin(), node_parents.end(), 0);
        node_ranks = vector<int>(edges.size() + 1, 1);

        for (auto& edge : edges) {
            // if parents of two nodes are same, it means that they already connected
            if (find_node_parent(edge[0]) == find_node_parent(edge[1]))
                return edge;
            connect_nodes(edge[0], edge[1]);
        }
        return {-1, -1};
    }

    int find_node_parent(int& node) {
        int curr_parent = node_parents[node];
        while (curr_parent != node_parents[curr_parent]) {
            node_parents[curr_parent] = node_parents[node_parents[curr_parent]];
            curr_parent = node_parents[curr_parent];
        }
        return curr_parent;
    }

    void connect_nodes(int& node_1, int& node_2) {
        int node_1_parent = find_node_parent(node_1);
        int node_2_parent = find_node_parent(node_2);

        if (node_ranks[node_1_parent] > node_ranks[node_2_parent]) {
            node_parents[node_2_parent] = node_1_parent;
            node_ranks[node_1_parent] += node_ranks[node_2_parent];
        } else {
            node_parents[node_1_parent] = find_node_parent(node_2_parent);
            node_ranks[node_2_parent] += node_ranks[node_1_parent];
        }
    }

private:
    vector<int> node_parents;
    vector<int> node_ranks;
};
