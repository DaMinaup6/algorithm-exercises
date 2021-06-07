# -----------------------------------------
# Model Solution: BFS
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://leetcode.com/problems/evaluate-division/discuss/558919/Python-3-DFS
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1, Graph Construction, var_relation_dict[var] = (ratio, next_var)
        var_relation_dict = defaultdict(list)
        for index, equation in enumerate(equations):
            var_1, var_2 = equation
            ratio = values[index]
            # var_relation_dict[key_var] = (ratio, val_var), where key_var * ratio == val_var
            var_relation_dict[var_1].append((1 / ratio, var_2))
            var_relation_dict[var_2].append((ratio, var_1))

        # 2, Pick a root for each component, set root value to 1 and compute the rest values
        var_ratio_root_dict = {}
        vars_to_compute = set(var_relation_dict.keys())
        while len(vars_to_compute) > 0:
            root = vars_to_compute.pop()

            ratio_vars = deque([(1, root)])
            while len(ratio_vars) > 0:
                ratio, var = ratio_vars.popleft()
                var_ratio_root_dict[var] = (ratio, root)
                # e.g. now we have var_relation_dict = { "a": (3, "b"), "b": (2, "c") }, which means a * 3 == b and b * 2 == c, and now root == "a"
                #
                #      at first iteration, var == "a" and ratio == 1 => var_ratio_root_dict["a"] == 1
                #      for next_var == "b", next_ratio would be 3 so we have ratio * next_ratio == 3
                #      then we get var_ratio_root_dict["b"] == (3, "a") and ratio_vars == [(3, "b")]
                #
                #      after previous iteration, we have var == "b" and ratio == 3
                #      for next_var == "c", next_ratio would be 2 so we have ratio * next_ratio == 6
                #      then we get var_ratio_root_dict["c"] == (6, "a") and ratio_vars == [] so this while loop stops here
                for next_ratio, next_var in var_relation_dict[var]:
                    if next_var in vars_to_compute:
                        ratio_vars.append((ratio * next_ratio, next_var))
                        vars_to_compute.remove(next_var)

        # 3, Query
        query_results = []
        for var_1, var_2 in queries:
            if var_1 in var_ratio_root_dict and var_2 in var_ratio_root_dict and var_ratio_root_dict[var_1][1] == var_ratio_root_dict[var_2][1]:
                query_results.append(var_ratio_root_dict[var_1][0] / var_ratio_root_dict[var_2][0])
            else:
                query_results.append(-1)
        return query_results
