# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(1)
# -----------------------------------------
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province_nums = 0
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected[0])):
                if self.directly_connected(isConnected, i, j):
                    self.spread(isConnected, i, j)
                    province_nums += 1
        for i in range(len(isConnected)):
            if self.directly_connected(isConnected, i, i):
                province_nums += 1

        return province_nums
    
    def directly_connected(self, isConnected, i, j):
        return 0 <= i < len(isConnected) and 0 <= j < len(isConnected[0]) and isConnected[i][j] == 1
    
    def spread(self, isConnected, i, j):
        if self.directly_connected(isConnected, i, j):
            isConnected[i][i] = isConnected[j][j] = isConnected[i][j] = isConnected[j][i] = 0
            for k in range(len(isConnected)):
                self.spread(isConnected, i, k)
                self.spread(isConnected, j, k)

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n^2)
# Space Complexity: O(n)
# -----------------------------------------
# Ref: https://blog.csdn.net/Orientliu96/article/details/104200380
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited_cities = set()
        def dfs(city):
            for other_city, connected in enumerate(isConnected[city]):
                if connected and other_city not in visited_cities:
                    visited_cities.add(other_city)
                    dfs(other_city)
        provinces = 0
        for city in range(len(isConnected)):
            if city not in visited_cities:
                visited_cities.add(city)
                dfs(city)
                provinces += 1
        return provinces
