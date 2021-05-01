# -----------------------------------------
# My Solution
#
# Time  Complexity: O(mlog(m) + nlog(n) + m + n)
# Space Complexity: O(1)
# -----------------------------------------
# m := len(houses), n := len(heaters)
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        min_radius_needed = 0
        curr_heater_index = 0
        for house_position in houses:
            # For sorted houses and heaters, if heater_j is the closest heater to house_i, then the closet heater to house_(i + 1) must be heater_j or heater_(j + 1) or heater_(j + 2) or ...
            while curr_heater_index < len(heaters) - 1 and abs(house_position - heaters[curr_heater_index]) >= abs(house_position - heaters[curr_heater_index + 1]):
                curr_heater_index += 1
            min_radius_needed = max(min_radius_needed, abs(house_position - heaters[curr_heater_index]))

        return min_radius_needed
