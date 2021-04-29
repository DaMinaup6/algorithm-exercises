# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n) + n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        citations_len = len(citations)
        for index, citation in enumerate(citations):
            # e.g. citations == [0,1,3,5,6]
            # if we want h_index == 5, which means we need to have at least 5 papers with at least 5 citations
            # since citations sorted, check first element, if first element >= 5 then the rest element must be greater than 5,
            # so we can say that we must have h_index == 5
            # apply same rule for rest elements then we can calculate the h_index
            citations_need_num = citations_len - index
            if citation >= citations_need_num:
                return citations_need_num
        return 0

# -----------------------------------------
# Model Solution: Sorting + Binary Search
#
# Time  Complexity: O(nlog(n) + log(n))
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://blog.csdn.net/fuxuemingzhu/article/details/82949663
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

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
