# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for num in range(1, n + 1):
            string = ''
            if num % 3 == 0:
                string += 'Fizz'
            if num % 5 == 0:
                string += 'Buzz'
            if len(string) == 0:
                string = str(num)
            arr.append(string)
        
        return arr
