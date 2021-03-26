# -----------------------------------------
# My Solution
#
# Time  Complexity: O(n * n!)
# Space Complexity: O(n^2)
# -----------------------------------------
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited_cells = set()
        def be_attacked(i, j):
            return any(cell[0] == i or cell[1] == j or abs(cell[0] - i) == abs(cell[1] - j) for cell in visited_cells)

        valid_combinations = []
        def backtracking(layer):
            if layer == n:
                valid_combinations.append(list(visited_cells))
                return
            for i in range(n):
                if not be_attacked(i, layer):
                    visited_cells.add((i, layer))
                    backtracking(layer + 1)
                    visited_cells.remove((i, layer))
        backtracking(0)

        answers = []
        for combination in valid_combinations:
            board = [['.'] * n for _ in range(n)]
            for position in combination:
                board[position[0]][position[1]] = 'Q'
            answers.append(map(lambda row: ''.join(row), board))
        return answers

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(n!)
# Space Complexity: O(n)
# -----------------------------------------
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def could_place(row, col):
            return not cols[col] and not hill_diagonals[row - col] and not dale_diagonals[row + col]
        
        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = True
            hill_diagonals[row - col] = True
            dale_diagonals[row + col] = True
        
        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = False
            hill_diagonals[row - col] = False
            dale_diagonals[row + col] = False
        
        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)
        
        def backtrack(row):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)
        
        cols = [False] * n
        hill_diagonals = [False] * (2 * n - 1)
        dale_diagonals = [False] * (2 * n - 1)
        queens = set()
        output = []
        backtrack(0)
        return output
