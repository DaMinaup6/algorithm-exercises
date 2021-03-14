# -----------------------------------------
# My Solution: Brute Force
#
# Time  Complexity: O(mn)
# Space Complexity: O(1)
# -----------------------------------------
# m := extraStudents, n := len(classes)
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        for _ in range(extraStudents):
            max_top_up = [-1, 0]
            for class_index, class_info in enumerate(classes):
                if class_info[0] == class_info[1]:
                    continue

                top_up = (class_info[0] + 1) / (class_info[1] + 1) - class_info[0] / class_info[1]
                if top_up > max_top_up[1]:
                    max_top_up = [class_index, top_up]
            classes[max_top_up[0]][0] += 1
            classes[max_top_up[0]][1] += 1

        total_sum = 0
        for class_info in classes:
            total_sum += class_info[0] / class_info[1]
        
        return total_sum / len(classes)

# -----------------------------------------
# Model Solution: Priority Queue + Greedy
#
# Time  Complexity: O((m + n) * log(n))
# Space Complexity: O(n)
# -----------------------------------------
# m := extraStudents, n := len(classes)
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = []
        for passed, total in classes:
            heapq.heappush(pq, (passed / total - (passed + 1) / (total + 1), passed, total))

        while extraStudents > 0:
            _, passed, total = heapq.heappop(pq)
            passed += 1
            total  += 1
            heapq.heappush(pq, (passed / total - (passed + 1) / (total + 1), passed, total))

            extraStudents -= 1
        
        return sum(passed / total for _, passed, total in pq) / len(classes)
