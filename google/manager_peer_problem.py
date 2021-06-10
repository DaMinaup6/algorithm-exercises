'''
Design a data structure to support following functions:
1. setManager(A, B) sets A as a direct manager of B
2. setPeer(A, B) sets A as a colleague of B. After that, A and B will have the same direct Manager.
3. query(A, B) returns if A is in the management chain of B.
Every person only has 1 direct manager.
'''

# -----------------------------------------
# Model Solution: Disjoint Set
#
# Space Complexity: O(n)
# -----------------------------------------
# n := number of employees
# Ref: https://massivealgorithms.blogspot.com/2016/08/google-manager-peer-problem.html
class ManagerPeer:
    def __init__(self):
        self.peer_head = {}
        self.peer_head_manager = {}

    # DEBUG
    def show_info(self):
        print("self.peer_head:        ", self.peer_head)
        print("self.peer_head_manager:", self.peer_head_manager)

    # Time Complexity: O(1)
    def init_peer(self, employ):
        if employ not in self.peer_head:
            self.peer_head[employ] = employ

    # Time Complexity: amortized O(1)
    def find_peer_head(self, employee):
        self.init_peer(employee)
        # path compression
        if self.peer_head[employee] != employee:
            self.peer_head[employee] = self.find_peer_head(self.peer_head[self.peer_head[employee]])
        return self.peer_head[employee]

    # Time Complexity: amortized O(1)
    def set_manager(self, manager, employee):
        self.init_peer(manager)
        self.init_peer(employee)

        employee_peer_head = self.find_peer_head(employee)
        self.peer_head_manager[employee_peer_head] = manager

    # Time Complexity: amortized O(1)
    def set_peer(self, employee_1, employee_2):
        self.init_peer(employee_1)
        self.init_peer(employee_2)

        employee_1_peer_head = self.find_peer_head(employee_1)
        employee_2_peer_head = self.find_peer_head(employee_2)
        if employee_1_peer_head in self.peer_head_manager:
            self.peer_head[employee_2_peer_head] = employee_1_peer_head
        else:
            self.peer_head[employee_1_peer_head] = employee_2_peer_head

    # Time Complexity: O(n)
    def is_manager_of(self, manager_candidate, employee):
        employee_peer_head = self.find_peer_head(employee)
        while employee_peer_head in self.peer_head_manager:
            if self.peer_head_manager[employee_peer_head] == manager_candidate:
                return True
            employee_peer_head = self.peer_head_manager[employee_peer_head]
        return False

#     E
#     |
#     D
#     |
# [A, B, C]
api = ManagerPeer()
api.set_manager("D", "A")
api.set_peer("A", "B")
api.set_peer("C", "B")
api.set_manager("E", "D")
print(api.is_manager_of("E", "C") == True)
print(api.is_manager_of("D", "A") == True)
print(api.is_manager_of("E", "D") == True)
print(api.is_manager_of("D", "B") == True)
print(api.is_manager_of("A", "B") == False)
# api.show_info()

#           H
#           |
# [A, B, C, D, E, F, G]
api = ManagerPeer()
api.set_peer("D", "C")
api.set_peer("A", "B")
api.set_peer("B", "C")
api.set_peer("D", "E")
api.set_peer("E", "F")
api.set_peer("G", "F")
api.set_manager("H", "C")
print(api.is_manager_of("H", "G") == True)
print(api.is_manager_of("A", "F") == False)
# api.show_info()

# A
# |
# B
# |
# C
api = ManagerPeer()
api.set_manager("A", "B")
api.set_manager("B", "C")
print(api.is_manager_of("A", "C") == True)
# api.show_info()

#     A
#     |
#     B
#     |
# [C, D, E]
api = ManagerPeer()
api.set_manager("A", "B")
api.set_manager("B", "C")
api.set_peer("D", "C")
api.set_peer("E", "C")
print(api.is_manager_of("B", "E") == True)
# api.show_info()
