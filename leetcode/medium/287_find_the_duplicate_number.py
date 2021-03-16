# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        checked_set = set()
        for num in nums:
            if num in checked_set:
                return num
            checked_set.add(num)

        return None

# -----------------------------------------
# Floyd's Tortoise and Hare (Cycle Detection)
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare

'''
steps before cycle: m
cycle length:       n
if n > m:
    when tortoise reaches cycle (set position 0 to start point of the cycle), hare already reaches m
    so they will meet at n - m because 0 + (n - m) == m + 2(n - m) % n == (2n - m) % n == n % n + (n - m) % n == n - m
    then distance from duplicated point is m
elif n == m:
    when tortoise reaches cycle (set position 0 to start point of the cycle), hare already reaches m, which also 0
    then distance from duplicated point is m
else: n < m:
    when tortoise reaches cycle (set position 0 to start point of the cycle), hare already reaches m % n
    so they will meet at n - (m % n)
    then distance from duplicated point is m because if we add m, then (n - (m % n) + m) % n == (n % n + (m % n) - (m % n)) == 0, that's why the distance to duplicated point is m
'''
