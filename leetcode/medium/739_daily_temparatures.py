# -----------------------------------------
# My Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
import heapq

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        output = [0] * len(T)
        pq = []
        
        for curr_idx in range(len(T)):
            heapq.heappush(pq, (T[curr_idx], curr_idx))
            while len(pq) > 0 and T[curr_idx] > pq[0][0]:
                _, prev_idx = heapq.heappop(pq)
                output[prev_idx] = curr_idx - prev_idx
                
        return output

# -----------------------------------------
# Stack
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        output = [0] * len(T)
        stack  = []
        for curr_idx in range(len(T)):
            while len(stack) > 0 and T[curr_idx] > stack[-1][0]:
                _, prev_idx = stack.pop()
                output[prev_idx] = curr_idx - prev_idx

            stack.append((T[curr_idx], curr_idx))
                
        return output
