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
        # since one envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height,
        # i.e. [1, 2] can fit into [3, 4] but cannot fit into [1, 3]
        # so we need to sort envelopes by (width, -height)
        # e.g. envelopes == [[1, 1], [1, 2], [1, 3]]
        #      obviously the answer is 1, but if just do envelopes.sort() and apply patience sort then we get answer 3, which is wrong
        #      so after envelopes.sort(key=lambda envelope: (envelope[0], -envelope[1])) we get envelopes == [[1, 3], [1, 2], [1, 1]]
        #      this time patience sort would give us correct answer
        envelopes.sort(key=lambda envelope: (envelope[0], -envelope[1]))
        patience_sort_list = []
        for _, height in envelopes:
            height_index = bisect.bisect_left(patience_sort_list, height)
            if height_index == len(patience_sort_list):
                patience_sort_list.append(height)
            else:
                patience_sort_list[height_index] = height

        return len(patience_sort_list)
