# -----------------------------------------
# My Solution
#
# Time  Complexity: O()
# Space Complexity: O(n)
# -----------------------------------------
# m := len(price) == len(needs), n := len(special)
# TODO: Check time complexity
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        checked_special = []
        for offer in special:
            original_price = 0
            for index in range(len(price)):
                original_price += offer[index] * price[index]
            if original_price > offer[-1]:
                checked_special.append(offer)

        original_total_price = 0
        for index, need in enumerate(needs):
            original_total_price += need * price[index]

        min_price = original_total_price
        def dfs(curr_price, curr_needs):
            nonlocal min_price

            if all(need == 0 for need in curr_needs):
                min_price = min(min_price, curr_price)
                return

            no_offer_used = True
            for offer in checked_special:
                next_needs  = curr_needs[:]
                offer_valid = True
                for index in range(len(needs)):
                    next_needs[index] -= offer[index]
                    if offer[index] > curr_needs[index]:
                        offer_valid = False
                if offer_valid:
                    dfs(curr_price + offer[-1], next_needs)
                    no_offer_used = False

            if no_offer_used:
                remain_total_price = 0
                for index, need in enumerate(curr_needs):
                    remain_total_price += need * price[index]
                dfs(curr_price + remain_total_price, [0] * len(needs))

        dfs(0, needs)
        return min_price
