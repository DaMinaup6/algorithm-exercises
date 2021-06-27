# -----------------------------------------
# Model Solution: DFS
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# n := len(prevRoom)
# Ref:
# a) https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/discuss/1299618/Python3.-Short-dfs.
# b) https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/discuss/1299540/PythonC%2B%2B-clean-DFS-solution-with-explanation
# c) https://leetcode-cn.com/problems/count-ways-to-build-rooms-in-an-ant-colony/solution/tong-ji-wei-yi-qun-gou-zhu-fang-jian-de-uqhn7/
from collections import defaultdict
from math import comb

class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10 ** 9 + 7

        rooms_tree = defaultdict(list)
        for room in range(1, len(prevRoom)):
            rooms_tree[prevRoom[room]].append(room)

        def dfs(room):
            total_edges  = 0
            orders_count = 1
            for next_room in rooms_tree[room]:
                child_edges, child_orders_count = dfs(next_room)
                total_edges += child_edges
                orders_count = (orders_count * comb(total_edges, child_edges) * child_orders_count) % MOD
            return (total_edges + 1, orders_count)
            
        return dfs(0)[1]
