# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://zxi.mytechroad.com/blog/graph/leetcode-685-redundant-connection-ii/
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [0] * (len(edges) + 1)
        dup_parent_edge_1 = [] # first edge which causes duplicated parent
        dup_parent_edge_2 = [] # last  edge which causes duplicated parent
        dup_parent_found  = False
        for edge in edges:
            parent, node = edge
            if parents[node] > 0:
                dup_parent_edge_1 = [parents[node], node]
                dup_parent_edge_2 = [parent, node]
                dup_parent_found  = True
                # delete last edge which causes duplicated parent
                edge[0] = edge[1] = -1
                break
            else:
                parents[node] = parent

        parents = [0] * (len(edges) + 1)
        def in_cycle(node):
            parent = parents[node]
            while parent != 0: # 0 means no parent or parent not assigned yet
                if parent == node:
                    return True
                parent = parents[parent]
            return False

        for edge in edges:
            parent, node = edge
            if parent < 0: # edge deleted in previous check since it causes duplicated parent
                continue
            parents[node] = parent
            if in_cycle(node):
                # if duplicated parent exists then it means cycle is caused by the first edge which causes duplicated parent, if no duplicated parent then just return edge causes cycle
                # p.s. the cycle cannot be caused by last edge which causes duplicated parent since we already deleted in previous check
                return dup_parent_edge_1 if dup_parent_found else edge

        # no cycle detected so just return the last edge which causes duplicated parent since if there are multiple answers, return the answer that occurs last in the given 2D-array
        return dup_parent_edge_2
