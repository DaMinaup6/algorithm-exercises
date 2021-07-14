# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# n := number of intervals
#
# Ref: https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b933#analysis
from collections import defaultdict

def calc_ans():
    n, c = [int(char) for char in input().split(' ')]

    cut_points_addition = defaultdict(int)
    for _ in range(n):
        l, r = [int(char) for char in input().split(' ')]
        # cut at l creates no additional interval so use l + 1
        cut_points_addition[l + 1] += 1
        # subtract number of r since number of overlaping intervals decreases after r
        cut_points_addition[r] -= 1
    cut_points = sorted(cut_points_addition.keys())

    # use cut points to calculate number of overlaping intervals
    overlaping_number_counter = defaultdict(int)
    curr_overlaping_number = cut_points_addition[cut_points[0]]
    for index in range(1, len(cut_points)):
        prev_endpoint = cut_points[index - 1]
        curr_endpoint = cut_points[index]

        overlaping_number_counter[curr_overlaping_number] += curr_endpoint - prev_endpoint
        curr_overlaping_number += cut_points_addition[curr_endpoint]
    
    additional_intervals_count = 0
    for overlaping_number in sorted(overlaping_number_counter.keys(), reverse=True):
        cur_candidates_count = overlaping_number_counter[overlaping_number]
        additional_intervals_count += overlaping_number * min(cur_candidates_count, c)
        c -= cur_candidates_count
        if c <= 0:
            break
    return n + additional_intervals_count

t = int(input())
for case_index in range(1, t + 1):
    print("Case #{}: {}".format(case_index, calc_ans()))
