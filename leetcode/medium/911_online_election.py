# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n + qlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# n := len(persons) == len(times), q := number of queries
import bisect

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.time_leader_dict = {}

        vote_count = [0] * (len(persons) + 1)
        vote_count[persons[0]] += 1
        curr_leader = persons[0]

        self.time_leader_dict[times[0]] = curr_leader
        for index in range(1, len(times)):
            next_leader = persons[index]
            vote_count[next_leader] += 1
            if vote_count[next_leader] >= vote_count[curr_leader]:
                curr_leader = next_leader
            self.time_leader_dict[times[index]] = curr_leader

    def q(self, t: int) -> int:
        if t in self.time_leader_dict:
            return self.time_leader_dict[t]

        time_index = bisect.bisect_left(self.times, t)
        return self.time_leader_dict[self.times[time_index - 1]]
