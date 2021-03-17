# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^3)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda person: (-person[0], person[1]))
        output = []
        for person in people:
            if len(output) == 0:
                output.append(person)
                continue

            non_shorter_count = 0
            for index in range(len(output)):
                if output[index][0] >= person[0]:
                    non_shorter_count += 1

                if non_shorter_count == person[1]:
                    output.insert(index + 1, person)
                    break
                elif non_shorter_count > person[1]:
                    output.insert(index, person)
                    break
                elif index == len(output) - 1:
                    output.append(person)

        return output

# -----------------------------------------
# Enhanced Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=HKHkzKvb0J4
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda person: (-person[0], person[1]))
        output = []
        for person in people:
            output.insert(person[1], person)

        return output
