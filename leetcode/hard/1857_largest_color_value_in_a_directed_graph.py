# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(m + n)
# Space Complexity: O(m + n)
# -----------------------------------------
# m := len(edges), n := len(colors)
# Ref: https://leetcode.com/problems/largest-color-value-in-a-directed-graph/discuss/1198971/The-key-to-solve-this-problem-without-TLE-Python3-O(V%2BE)
import collections
import functools

class Node:
    def __init__(self):
        self.node_num = -1
        self.parents  = set()
        self.children = set()

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return 1
        
        colors = list(colors)
        for index, color in enumerate(colors):
            colors[index] = ord(color) - ord('a')

        nodes = collections.defaultdict(Node)
        for source, target in edges:
            source_node = nodes[source]
            target_node = nodes[target]
            source_node.node_num = source
            target_node.node_num = target

            if target_node not in source_node.children:
                source_node.children.add(target_node)
            if source_node not in target_node.parents:
                target_node.parents.add(source_node)

        roots = []
        for node_num in nodes:
            if len(nodes[node_num].parents) == 0:
                roots.append(nodes[node_num])
        if len(roots) == 0:
            return -1

        @functools.lru_cache(None)
        def dfs(curr_node):
            if curr_node in visited_nodes:
                self.contains_cycle = True
                return [0] * 26
            visited_nodes.add(curr_node)

            curr_color   = colors[curr_node.node_num]
            colors_count = [0] * 26

            for child in curr_node.children:
                if self.contains_cycle:
                    return [0] * 26
                child_colors_count = dfs(child)
                for index in range(26):
                    colors_count[index] = max(colors_count[index], child_colors_count[index])

            colors_count[curr_color] += 1
            return colors_count

        self.contains_cycle = False
        max_color_count = 1
        for root in roots:
            visited_nodes   = set()
            max_color_count = max(max_color_count, max(dfs(root)))
            if self.contains_cycle:
                return -1

        return max_color_count
