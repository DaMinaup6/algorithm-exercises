# -----------------------------------------
# My Solution
# -----------------------------------------
# def get_possible_combinations(min, max, size):
#     combinations = []
#
#     def generate_combination(combination, min, max, size):
#         if size == 1:
#             combinations.append(combination)
#         else:
#             for num in range(min, max + 1):
#                 generate_combination(combination + [num], min, max, size - 1)
#
#     for num in range(min, max + 1):
#         generate_combination([num], min, max, size)
#
#     return combinations
#
# class Solution:
#     def closestCost(self, baseCosts, toppingCosts, target):
#         possible_costs = []
#         possible_topping_combinations = get_possible_combinations(0, 2, len(toppingCosts))
#
#         for base_cost in baseCosts:
#             if base_cost >= target:
#                 possible_costs.append(base_cost)
#                 continue
#             else:
#                 for possible_topping_combination in possible_topping_combinations:
#                     possible_cost = base_cost
#                     for idx in range(0, len(toppingCosts)):
#                         possible_cost += possible_topping_combination[idx] * toppingCosts[idx]
#                         if possible_cost >= target:
#                             break
#                     possible_costs.append(possible_cost)
#
#         min_diff = min(abs(possible_cost - target) for possible_cost in possible_costs)
#         return min([possible_cost for possible_cost in possible_costs if abs(target - possible_cost) == min_diff])

# -----------------------------------------
# Recursive
# -----------------------------------------
class Solution:
    def closet_cost_between(self, cost_1, cost_2, target):
        cost_1_diff = abs(target - cost_1)
        cost_2_diff = abs(target - cost_2)

        if cost_1_diff < cost_2_diff or cost_1_diff == cost_2_diff and cost_1 < cost_2:
            return cost_1
        else:
            return cost_2

    def get_closet_cost_with_topping(self, topping_idx, toppings, current_cost, closet_cost, target):
        if current_cost >= target or topping_idx == len(toppings):
            return self.closet_cost_between(closet_cost, current_cost, target)
        else:
            closet_cost_1 = self.get_closet_cost_with_topping(topping_idx + 1, toppings, current_cost + 0 * toppings[topping_idx], closet_cost, target)
            closet_cost_2 = self.get_closet_cost_with_topping(topping_idx + 1, toppings, current_cost + 1 * toppings[topping_idx], closet_cost, target)
            closet_cost_3 = self.get_closet_cost_with_topping(topping_idx + 1, toppings, current_cost + 2 * toppings[topping_idx], closet_cost, target)
            closet_cost = self.closet_cost_between(closet_cost, closet_cost_1, target)
            closet_cost = self.closet_cost_between(closet_cost, closet_cost_2, target)
            closet_cost = self.closet_cost_between(closet_cost, closet_cost_3, target)

            return closet_cost

    def closestCost(self, baseCosts, toppingCosts, target):
        closet_cost = float('inf')

        for base_cost in baseCosts:
            if base_cost >= target:
                closet_cost = self.closet_cost_between(closet_cost, base_cost, target)
                continue
            else:
                closet_cost_with_topping = self.get_closet_cost_with_topping(0, toppingCosts, base_cost, closet_cost, target)
                closet_cost = self.closet_cost_between(closet_cost, closet_cost_with_topping, target)

        return closet_cost

solution = Solution()
print(f"01. solution.closestCost([4], [9], 9)                                  ==   13: {solution.closestCost([4], [9], 9) == 13}")
print(f"02. solution.closestCost([2, 3], [4, 5, 100], 18)                      ==   17: {solution.closestCost([2, 3], [4, 5, 100], 18) == 17}")
print(f"03. solution.closestCost([5020, 1159], [1253, 5085, 4881, 2593], 6819) == 6345: {solution.closestCost([5020, 1159], [1253, 5085, 4881, 2593], 6819) == 6345}")
