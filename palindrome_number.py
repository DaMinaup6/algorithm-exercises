import math

def isPalindrome(x):
    num_str = str(x)
    if not num_str[0].isdigit():
        return False

    for idx in range(0, math.floor(len(num_str) / 2) + 1):
        if num_str[idx] != num_str[len(num_str) - 1 - idx]:
            return False
    return True
