# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# n := len(times)
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arrive_time_id = []
        leave_time_id  = []
        for friend_id, time in enumerate(times):
            arrive_time_id.append((time[0], friend_id))
            leave_time_id.append((time[1], friend_id))
        arrive_time_id.sort(reverse=True)
        leave_time_id.sort(reverse=True)

        seat_unoccupied = list(range(len(times)))
        friend_id_seat_occupied = {}
        for curr_time in range(max(arrive_time_id[0][0], leave_time_id[0][0]) + 1):
            while curr_time == leave_time_id[-1][0]:
                occupied_seat = friend_id_seat_occupied[leave_time_id[-1][1]]
                heapq.heappush(seat_unoccupied, occupied_seat)
                leave_time_id.pop()

            if curr_time == arrive_time_id[-1][0]:
                smallest_seat_unoccupied = heapq.heappop(seat_unoccupied)
                if arrive_time_id[-1][1] == targetFriend:
                    return smallest_seat_unoccupied

                friend_id_seat_occupied[arrive_time_id[-1][1]] = smallest_seat_unoccupied
                arrive_time_id.pop()

        return -1
