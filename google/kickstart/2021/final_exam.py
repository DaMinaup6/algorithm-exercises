# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(mlog(m + n) + nlog(n))
# Space Complexity: O(m + n)
# -----------------------------------------
# m := number of students, n := number of problem sets
#
# Ref: https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082bffc#analysis
import bisect

def update_diffs(index, skill):
    if skill in start_end_diff_mapping:
        if start_end_diff_mapping[skill] == skill:
            start_end_diff_mapping.pop(skill)
            start_diffs.pop(index)
        else:
            start_end_diff_mapping[start_diffs[index] + 1] = start_end_diff_mapping[start_diffs[index]]
            start_end_diff_mapping.pop(start_diffs[index])
            start_diffs[index] += 1
    elif start_end_diff_mapping[start_diffs[index]] == skill:
        start_end_diff_mapping[start_diffs[index]] -= 1
        if start_end_diff_mapping[start_diffs[index]] < start_diffs[index]:
            start_end_diff_mapping.pop(start_diffs[index])
            start_diffs.pop(index)
    elif start_diffs[index] < skill < start_end_diff_mapping[start_diffs[index]]:
        start_end_diff_mapping[skill + 1] = start_end_diff_mapping[start_diffs[index]]
        start_end_diff_mapping[start_diffs[index]] = skill - 1
        start_diffs.insert(index + 1, skill + 1)

def calc_ans():
    ans = []
    for skill in students:
        # either index == len(start_diffs) or start_diffs[index] > skill
        index = bisect.bisect_right(start_diffs, skill)

        # skill < start_diffs[0], remove start_diffs[0]
        if index == 0:
            ans.append(start_diffs[0])
            update_diffs(0, ans[-1])
        # start_diffs[index - 1] < skill <= start_end_diff_mapping[start_diffs[index - 1]]
        elif start_end_diff_mapping[start_diffs[index - 1]] >= skill:
            ans.append(skill)
            update_diffs(index - 1, ans[-1])
        # start_end_diff_mapping[start_diffs[index - 1]] < skill < start_diffs[index] but closer to start_end_diff_mapping[start_diffs[index - 1]]
        elif index == len(start_diffs) or skill - start_end_diff_mapping[start_diffs[index - 1]] <= start_diffs[index] - skill:
            ans.append(start_end_diff_mapping[start_diffs[index - 1]])
            update_diffs(index - 1, ans[-1])
        # skill < start_diffs[index]
        else:
            ans.append(start_diffs[index])
            update_diffs(index, ans[-1])
    return ' '.join([str(a) for a in ans])

t = int(input())
for i in range(1, t + 1):
    n, m = [int(char) for char in input().split(' ')]

    start_end_diff_mapping = {}
    for _ in range(n):
        diff_1, diff_2 = [int(char) for char in input().split(' ')]
        start_end_diff_mapping[diff_1] = diff_2
    start_diffs = sorted(start_end_diff_mapping.keys())
    students = [int(char) for char in input().split(' ')]

    print("Case #{}: {}".format(i, calc_ans()))
