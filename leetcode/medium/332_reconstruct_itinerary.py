# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=4udFSOWQpdg
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from_to_mapping = defaultdict(list)
        for ticket in tickets:
            from_to_mapping[ticket[0]].append(ticket[1])
        for _, to_airports in from_to_mapping.items():
            to_airports.sort(reverse=True)

        itinerary_list = []
        def dfs(airport):
            while len(from_to_mapping[airport]):
                next_airport = from_to_mapping[airport].pop()
                dfs(next_airport)
            itinerary_list.append(airport)
        dfs('JFK')
        return itinerary_list[::-1]
