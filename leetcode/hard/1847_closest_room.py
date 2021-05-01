# -----------------------------------------
# My Solution
#
# Time  Complexity: O(klog(kn) + nlog(n))
# Space Complexity: O(k + n)
# -----------------------------------------
# k := len(queries), n := len(rooms)

from collections import defaultdict
import bisect

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        # O(k)
        for index in range(len(queries)):
            queries[index].append(index)
        # O(klog(k))
        queries.sort(key=lambda query: (-query[1], query[0], query[2]))

        room_size_ids_dict = defaultdict(list)
        # O(n)
        for room_id, room_size in rooms:
            room_size_ids_dict[room_size].append(room_id)
        # O(nlog(n) + n)
        room_sizes = sorted(room_size_ids_dict.keys())

        # check query from largest min_size required
        # e.g. rooms == [[1, 1], [2, 1], [3, 1], [5, 4], [6, 5], [7, 6], [8, 4]], queries == [[4, 2], [9, 5]]
        #      check query [9, 5] first then [4, 2]
        #
        # check query [9, 5], add room_ids from size 5 and 6 to available_room_ids then get available_room_ids == [6, 7]
        # check query [4, 2], just need to add room_ids from size 4, which are [5, 8] to available_room_ids, so we get available_room_ids == [5, 6, 7, 8]
        # now available_room_ids must be rooms with room size larger than current min_size since we check from largest min_size to smaller ones
        available_room_ids = []
        prev_room_size_idx = len(room_sizes)
        room_ids = [-1] * len(queries)
        # O((k + n)log(n))
        for preferred, min_size, query_index in queries:
            if min_size > room_sizes[-1]:
                continue

            # This is at most O(nlog(n)) after k iterations since we check every room size at most one time, so each room_id would be added to
            # available_room_ids at most one time
            first_available_room_size_idx = bisect.bisect_left(room_sizes, min_size)
            for index in range(first_available_room_size_idx, prev_room_size_idx):
                for room_id in room_size_ids_dict[room_sizes[index]]:
                    bisect.insort(available_room_ids, room_id)
            prev_room_size_idx = first_available_room_size_idx

            # O(log(n))
            room_id_index = bisect.bisect_left(available_room_ids, preferred)
            # O(1)
            if room_id_index == 0:
                room_ids[query_index] = available_room_ids[0]
            elif room_id_index >= len(available_room_ids):
                room_ids[query_index] = available_room_ids[-1]
            elif abs(available_room_ids[room_id_index] - preferred) < abs(available_room_ids[room_id_index - 1] - preferred):
                room_ids[query_index] = available_room_ids[room_id_index]
            else:
                room_ids[query_index] = available_room_ids[room_id_index - 1]
        return room_ids
