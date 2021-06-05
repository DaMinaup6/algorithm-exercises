# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(Elog(V))
# Space Complexity: O(E)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=wmW8G8SrXDs
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_root = list(range(len(edges)))
        def find_union_root(node):
            if node != union_root[node]:
                union_root[node] = find_union_root(union_root[union_root[node]])
            return union_root[node]

        for edge in edges:
            # from 1-indexed to 0-indexed
            node_1 = edge[0] - 1
            node_2 = edge[1] - 1

            node_1_root, node_2_root = find_union_root(node_1), find_union_root(node_2)
            if node_1_root == node_2_root:
                return edge
            union_root[node_1_root] = node_2_root

        return [-1, -1]

# -----------------------------------------
# Model Solution: Union Find
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=FXWRE67PLL0
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [node for node in range(len(edges) + 1)]
        ranks   = [1] * (len(edges) + 1)

        def find_parent(node):
            parent = parents[node]
            while parent != parents[parent]:
                parents[parent] = parents[parents[parent]]
                parent = parents[parent]
            return parent

        # return False if node_1 and node_2 share same parent, means they already connected
        def union_nodes(node_1, node_2):
            parent_1, parent_2 = find_parent(node_1), find_parent(node_2)
            if parent_1 == parent_2:
                return False

            if ranks[parent_1] > ranks[parent_2]:
                parents[parent_2] = parent_1
                ranks[parent_1] += ranks[parent_2]
            else:
                parents[parent_1] = parent_2
                ranks[parent_2] += ranks[parent_1]
            return True

        for node_1, node_2 in edges:
            if not union_nodes(node_1, node_2):
                return [node_1, node_2]
        return []
