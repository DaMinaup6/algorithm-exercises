'''
There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together. (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together. The cost is the sum of the connection costs used. If the task is impossible, return -1.
'''

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(Elog(V))
# Space Complexity: O(E)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=wmW8G8SrXDs
class Solution:
    def minimumCost(self, N, connections):
        union_head = list(range(N))
        def find_union_head(node):
            if node != union_head[node]:
                union_head[node] = find_union_head(union_head[union_head[node]])
            return union_head[node]

        total_cost = 0
        for city_1, city_2, cost in sorted(connections, key=lambda connection: connection[2]):
            # from 1-indexed to 0-indexed
            city_1 -= 1
            city_2 -= 1

            city_1_union_head, city_2_union_head = find_union_head(city_1), find_union_head(city_2)
            if city_1_union_head == city_2_union_head:
                continue
            union_head[city_1_union_head] = city_2_union_head
            total_cost += cost

        return total_cost if len(set(union_head)) == 1 else -1

processor = Solution()
print(processor.minimumCost(3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]) == 6)
print(processor.minimumCost(4, [[1, 2, 3], [3, 4, 4]]) == -1)
