# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda envelope: (envelope[0], envelope[1]))
        max_count = [1] * len(envelopes)
        for index in range(1, len(envelopes)):
            curr_envelope = envelopes[index]
            for prev_index in range(index - 1, -1, -1):
                prev_envelope = envelopes[prev_index]
                if curr_envelope[0] > prev_envelope[0] and curr_envelope[1] > prev_envelope[1] and max_count[prev_index] + 1 > max_count[index]:
                    max_count[index] = max_count[prev_index] + 1

        return max(max_count)

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://zhuanlan.zhihu.com/p/67808970
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda envelope: (envelope[0], -envelope[1]))
        patience_sort_list = []
        for _, height in envelopes:
            prev_index = bisect.bisect_left(patience_sort_list, height)
            if prev_index == len(patience_sort_list):
                patience_sort_list.append(height)
            else:
                patience_sort_list[prev_index] = height

        return len(patience_sort_list)
