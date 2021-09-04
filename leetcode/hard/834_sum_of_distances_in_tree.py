# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/sum-of-distances-in-tree/solution/

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n
        ans = [0] * n
        def dfs1(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs1(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    # ans[x] - ans[y] == #(Y) - #(X) == (n - #(X)) - #(X)
                    ans[child] = ans[node] + (n - count[child]) - count[child]
                    dfs2(child, node)

        dfs1(0, None)
        dfs2(0, None)
        return ans
