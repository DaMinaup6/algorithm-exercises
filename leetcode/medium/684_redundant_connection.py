# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(Elog(V))
# Space Complexity: O(E)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=wmW8G8SrXDs
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_head = list(range(len(edges)))
        def find_union_head(node):
            if node != union_head[node]:
                union_head[node] = find_union_head(union_head[union_head[node]])
            return union_head[node]
        
        for edge in edges:
            # from 1-indexed to 0-indexed
            node_1 = edge[0] - 1
            node_2 = edge[1] - 1

            node_1_root, node_2_root = find_union_head(node_1), find_union_head(node_2)
            if node_1_root == node_2_root:
                return edge
            union_head[node_1_root] = node_2_root

        return [-1, -1]
