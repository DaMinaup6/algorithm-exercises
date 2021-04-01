# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(Elog(E))
# Space Complexity: O(E)
# -----------------------------------------
# E := len(edges)
# Ref
# a) https://github.com/changgyhub/leetcode_101/blob/master/LeetCode%20101%20-%20A%20LeetCode%20Grinding%20Guide%20(C%2B%2B%20Version).pdf
# b) https://www.youtube.com/watch?v=SGki2XeWBEo
# c) https://www.youtube.com/watch?v=wmW8G8SrXDs
import heapq

from collections import defaultdict

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for node_1, node_2, weight in edges:
            graph[node_1][node_2] = weight
            graph[node_2][node_1] = weight

        distance_to_zero = {0: 0}
        # how many nodes can be reached from u to v
        # e.g. reachable_nodes_between[(u, v)] == 3 means there are 3 nodes reachable from u to v
        # reachable_nodes_between[(u, v)] might not equal to reachable_nodes_between[(v, u)], one example is the example in problem description
        reachable_nodes_between = {}
        pq = [(0, 0)]
        while len(pq) > 0:
            distance, node = heapq.heappop(pq)
            # because heapq.heappush doesn't remove old pairs with the same neighbor so do a check here
            if distance > distance_to_zero[node]:
                continue

            for neighbor, weight in graph[node].items():
                # e.g. in the example of problem description, 10 nodes between 0 and 1, for 0 -> 1 there are 6 nodes reachable (since maxMoves is 6)
                #      and for 1 -> 0 there is 1 node reachable since there is only 1 move left after 0 reaches 1
                # Also distance is limited by maxMoves so there would be no negative numbers
                reachable_nodes_between[(node, neighbor)] = min(weight, maxMoves - distance)
                new_distance = distance + weight + 1
                # distance larger than maxMoves means not reachable from 0 so distance needs to be < maxMoves + 1
                if new_distance < distance_to_zero.get(neighbor, maxMoves + 1):
                    distance_to_zero[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))

        reachable_count = len(distance_to_zero) # only reachable nodes would be recorded in distance_to_zero
        for node_1, node_2, weight in edges:
            reachable_count += min(weight, reachable_nodes_between.get((node_1, node_2), 0) + reachable_nodes_between.get((node_2, node_1), 0))
        return reachable_count
