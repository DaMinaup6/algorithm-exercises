// -----------------------------------------
// Model Solution: Modified Djikstra's
//
// Time  Complexity: O(m + nlog(n))
// Space Complexity: O(m + n)
// -----------------------------------------
// m := edges.size(), n := passingFees.size()
//
// Ref: https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/discuss/1328989/Python3-Modified-Djikstra's
class Solution {
public:
    int minCost(int maxTime, vector<vector<int>>& edges, vector<int>& passingFees) {
        int cities_count = passingFees.size();

        vector<vector<pair<int, int>>> city_map_next_city_time(cities_count);
        for (int index = 0; index < edges.size(); ++index) {
            int city_1 = edges[index][0];
            int city_2 = edges[index][1];
            int travel = edges[index][2];

            city_map_next_city_time[city_1].push_back({city_2, travel});
            city_map_next_city_time[city_2].push_back({city_1, travel});
        }

        unordered_map<int, int> city_visited_time;
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> min_heap;
        min_heap.push({passingFees[0], 0, 0});
        while (!min_heap.empty()) {
            tuple<int, int, int> curr_info = min_heap.top();
            min_heap.pop();

            int curr_time = get<2>(curr_info);
            if (curr_time > maxTime)
                continue;

            int fee_spent = get<0>(curr_info);
            int curr_city = get<1>(curr_info);
            if (curr_city == cities_count - 1)
                return fee_spent;

            if (city_visited_time.find(curr_city) == city_visited_time.end() || city_visited_time[curr_city] > curr_time) {
                city_visited_time[curr_city] = curr_time;
                for (auto& pair_info : city_map_next_city_time[curr_city]) {
                    int next_city = pair_info.first;
                    int time_take = pair_info.second;
                    min_heap.push({fee_spent + passingFees[next_city], next_city, curr_time + time_take});
                }
            }
        }
        return -1;
    }
};
