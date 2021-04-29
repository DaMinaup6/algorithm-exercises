# -----------------------------------------
# Model Solution: Binary Search
#
# Time  Complexity: O(log(n))
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/82949663
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations_len = len(citations)
        left_pointer, right_pointer = 0, len(citations) - 1
        while left_pointer < right_pointer:
            middle_pointer  = (left_pointer + right_pointer) // 2
            middle_citation = citations[middle_pointer]
            citation_needed = citations_len - middle_pointer

            if middle_citation >= citation_needed:
                right_pointer = middle_pointer
            else:
                left_pointer = middle_pointer + 1

        return citations_len - right_pointer if citations[right_pointer] >= citations_len - right_pointer else 0
