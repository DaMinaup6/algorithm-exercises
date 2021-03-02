class Solution:
    def getCollisionTimes(self, cars):
        answer = [-1.0] * len(cars)
        candidate_list = []

        for car_index in range(len(cars) - 1, -1, -1):
            current_car = cars[car_index]

            # don't need faster cars "behind" (at farther position) current car
            while len(candidate_list) > 0 and current_car[1] <= cars[candidate_list[-1]][1]:
                candidate_list.pop()

            while len(candidate_list) > 0:
                candidate = candidate_list[-1]
                candidate_car  = cars[candidate]
                collision_time = (candidate_car[0] - current_car[0]) / (current_car[1] - candidate_car[1])
                if collision_time <= answer[candidate] or answer[candidate] < 0:
                    answer[car_index] = collision_time
                    break

                candidate_list.pop()

            candidate_list.append(car_index)

        return answer

processor = Solution()
print(f"processor.getCollisionTimes([[3, 2], [4, 4], [6, 3], [9, 1]]) == [6.00000, 5 / 3, 1.50000, -1.00000]: {processor.getCollisionTimes([[3, 2], [4, 4], [6, 3], [9, 1]]) == [6.00000, 5 / 3, 1.50000, -1.00000]}")
