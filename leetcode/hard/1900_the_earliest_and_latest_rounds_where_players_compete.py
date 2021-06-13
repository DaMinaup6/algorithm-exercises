# -----------------------------------------
# My Solution: Brute Force
#
# Time  Complexity: O(2^n + nlog(n) * 2^(n // 2))
# Space Complexity: O(2^(n // 2))
# -----------------------------------------
from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        def add_next_tournament(curr_tournament, next_tournaments, next_tournament, index):
            if curr_tournament[index] in (firstPlayer, secondPlayer):
                next_tournament[index] = curr_tournament[index]
                next_tournaments.append(next_tournament[:])
            elif curr_tournament[-1 - index] in (firstPlayer, secondPlayer):
                next_tournament[index] = curr_tournament[-1 - index]
                next_tournaments.append(next_tournament[:])
            else:
                next_tournament[index] = curr_tournament[index]
                next_tournaments.append(next_tournament[:])
                next_tournament[index] = curr_tournament[-1 - index]
                next_tournaments.append(next_tournament[:])

        earliest_round, latest_round = float('inf'), -float('inf')
        # list all possibilities recursively
        @lru_cache(None)
        def dfs(curr_tournament, curr_round):
            nonlocal earliest_round, latest_round

            if len(curr_tournament) == 1:
                return
            for index in range(len(curr_tournament) // 2):
                if (curr_tournament[index], curr_tournament[-1 - index]) == (firstPlayer, secondPlayer):
                    earliest_round = min(earliest_round, curr_round)
                    latest_round   = max(latest_round,   curr_round)
                    return

            # generate all outcomes for next tournament
            # e.g. curr_tournament == [1, 2, 3, 4]
            #      then we have possible outcomes [[1, 2], [3, 2], [1, 4], [3, 4]] for next tournament
            tmp_next_tournament = [0] * (len(curr_tournament) // 2)
            if len(curr_tournament) % 2 == 1:
                tmp_next_tournament.append(curr_tournament[len(curr_tournament) // 2])
            possible_tournaments = [tmp_next_tournament]
            for index in range(len(curr_tournament) // 2):
                next_tournaments = []
                for next_tournament in possible_tournaments:
                    add_next_tournament(curr_tournament, next_tournaments, next_tournament, index)
                possible_tournaments = next_tournaments

            for next_tournament in possible_tournaments:
                dfs(tuple(sorted(next_tournament)), curr_round + 1)

        dfs(tuple(range(1, n + 1)), 1)
        return [earliest_round, latest_round]
