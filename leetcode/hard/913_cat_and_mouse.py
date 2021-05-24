# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n^4)
# Space Complexity: O(n^3)
# -----------------------------------------
# Ref: https://leetcode.com/problems/cat-and-mouse/discuss/1023914/Python-Top-Down-DP-beats-99
from functools import lru_cache

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        @lru_cache(None)
        def helper(turn, mouse_node, cat_node):
            # If the mouse or the cat will win, they will do so in less than 2n turns where n is the number of nodes
            if turn == 0:
                return 0

            results = set()
            if turn % 2 == 0:
                # Mouse's turn
                if 0 in graph[mouse_node]:
                    return 1
                for next_mouse_node in graph[mouse_node]:
                    results.add(helper(turn - 1, next_mouse_node, cat_node))
                    if 1 in results:
                        return 1
            else:
                # Cat's turn
                if mouse_node in graph[cat_node] or cat_node == mouse_node:
                    return 2
                for next_cat_node in graph[cat_node] - {0}:
                    results.add(helper(turn - 1, mouse_node, next_cat_node))
                    if 2 in results:
                        return 2
            return min(results)

        total_turns = len(graph) * 2
        graph = {node: set(next_nodes) for node, next_nodes in enumerate(graph)}
        return helper(total_turns, 1, 2)
