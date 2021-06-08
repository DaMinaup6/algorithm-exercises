# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        distance_from_left  = [float('inf')] * len(seats)
        distance_from_right = [float('inf')] * len(seats)
        for index in range(len(seats)):
            if seats[index] == 1:
                distance_from_left[index] = 0
            elif index > 0:
                distance_from_left[index] = distance_from_left[index - 1] + 1
        for index in range(len(seats) - 1, -1, -1):
            if seats[index] == 1:
                distance_from_right[index] = 0
            elif index < len(seats) - 1:
                distance_from_right[index] = distance_from_right[index + 1] + 1

        max_distance = -float('inf')
        for index in range(len(seats)):
            max_distance = max(max_distance, min(distance_from_left[index], distance_from_right[index]))
        return max_distance

# -----------------------------------------
# Model Solution: Two Pointers
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        people_position = (i for i, seat in enumerate(seats) if seat)
        prev_person_position, next_person_position = None, next(people_position)

        max_distance = 0
        for index, seat in enumerate(seats):
            if seat == 1:
                prev_person_position = index
            else:
                while next_person_position is not None and next_person_position < index:
                    next_person_position = next(people_position, None)
                left_distance  = float('inf') if prev_person_position is None else index - prev_person_position
                right_distance = float('inf') if next_person_position is None else next_person_position - index
                max_distance   = max(max_distance, min(left_distance, right_distance))
        return max_distance
