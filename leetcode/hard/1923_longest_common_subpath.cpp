// -----------------------------------------
// Model Solution: Binary Search + Rabin-Karp's Rolling Hash + Collision Check
//
// Time  Complexity: O(slog(p))
// Space Complexity: O(s)
// -----------------------------------------
// s := sum(paths[i].length), p := min(paths[i].length)
//
// Ref: https://leetcode.com/problems/longest-common-subpath/discuss/1314826/Rolling-Hash-%2B-Collision-Check
class Solution {
public:
    int longestCommonSubpath(int n, vector<vector<int>>& paths) {
        int min_common_subpath = 0;
        int max_common_subpath = min_element(paths.begin(), paths.end(), [](const auto& path_1, const auto& path_2) { return path_1.size() < path_2.size(); })->size();
        while (min_common_subpath <= max_common_subpath) {
            int common_subpath_length = (min_common_subpath + max_common_subpath) / 2;

            unordered_map<int, vector<int>> curr_seen_subpaths_start_index_map;
            for (int path_index = 0; path_index < paths.size(); ++path_index) {
                unordered_map<int, vector<int>> next_seen_subpaths_start_index_map;
                long long subpath_hash_value = 0;
                long long curr_power = 1;

                for (int city_index = 0; city_index < paths[path_index].size(); ++city_index) {
                    subpath_hash_value = ((subpath_hash_value * BASE) % MOD + paths[path_index][city_index]) % MOD;
                    if (city_index >= common_subpath_length)
                        subpath_hash_value = (subpath_hash_value - (paths[path_index][city_index - common_subpath_length] * curr_power) % MOD + MOD) % MOD;
                    else
                        curr_power = (curr_power * BASE) % MOD;

                    if (city_index >= common_subpath_length - 1) {
                        if (path_index == 0) {
                            next_seen_subpaths_start_index_map[subpath_hash_value].push_back(city_index - common_subpath_length + 1);
                        } else if (curr_seen_subpaths_start_index_map.count(subpath_hash_value) > 0) {
                            // Collision Check
                            for (auto start_index : curr_seen_subpaths_start_index_map[subpath_hash_value]) {
                                if (equal(paths[0].begin() + start_index, paths[0].begin() + start_index + common_subpath_length, paths[path_index].begin() + city_index - common_subpath_length + 1)) {
                                    next_seen_subpaths_start_index_map[subpath_hash_value].push_back(start_index);
                                    break;
                                }
                            }
                        }
                    }
                }

                swap(curr_seen_subpaths_start_index_map, next_seen_subpaths_start_index_map);
                if (curr_seen_subpaths_start_index_map.empty())
                    break;
            }

            if (curr_seen_subpaths_start_index_map.empty())
                max_common_subpath = common_subpath_length - 1;
            else
                min_common_subpath = common_subpath_length + 1;
        }

        return max_common_subpath;
    }

private:
    static const int BASE = 100001;
    static const int MOD  = 1000000007;
};
