# -----------------------------------------
# My Solution: Dynamic Programming
#
# Time  Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)

        # e.g. cardPoints == [1, 2, 7, 3, 2, 1, 1], k == 3
        # the answer would be either
        # 1. select 0 card from left side,       k cards from right side: cardPoints[:0] + cardPoints[-k:]
        # 2. select 1 card from left side, (k - 1) cards from right side: cardPoints[:1] + cardPoints[-(k - 1):]
        # ...
        # k. select k card from left side,       0 cards from right side: cardPoints[:k] + cardPoints[len(cardPoints):]
        # so use left_sum and right_sum to store curr sum on both side
        left_sum  = 0
        right_sum = sum(cardPoints[-k:])
        max_score = right_sum
        for left_index in range(k):
            left_sum  += cardPoints[left_index]
            right_sum -= cardPoints[len(cardPoints) - k + left_index]
            max_score  = max(max_score, left_sum + right_sum)
        return max_score
