# -----------------------------------------
# My Solution
#
# Time  Complexity: O(12 * 60 * 60 * 3)
# Space Complexity: O(1)
# -----------------------------------------
# Note: This solution only solves two test sets
def calc_time(angle_1, angle_2, angle_3):
    if angle_1 == angle_2 == angle_3:
        return '0 0 0 0'
    else:
        for h in range(12):
            for m in range(60):
                for s in range(60):
                    nano_s  = (h * 3600 + m * 60 + s) * 1e9
                    angle_h = nano_s % (360 * 12 * 1e10)
                    angle_m = (nano_s * 12) % (360 * 12 * 1e10)
                    angle_s = (nano_s * 720) % (360 * 12 * 1e10)
                    tmp_angle_1, tmp_angle_2, tmp_angle_3 = sorted([angle_h, angle_m, angle_s])

                    for standard_angle in [angle_1, angle_2, angle_3]:
                        standard_diff = standard_angle - tmp_angle_1
                        new_angle_1, new_angle_2, new_angle_3 = sorted([(angle_1 - standard_diff) % (360 * 12 * 1e10), (angle_2 - standard_diff) % (360 * 12 * 1e10), (angle_3 - standard_diff) % (360 * 12 * 1e10)])
                        if tmp_angle_1 == new_angle_1 and tmp_angle_2 == new_angle_2 and tmp_angle_3 == new_angle_3:
                            return ' '.join([str(h), str(m), str(s), '0'])
    return '0 0 0 0'

t = int(input())
for i in range(1, t + 1):
    angle_1, angle_2, angle_3 = [int(s) for s in input().split(" ")]
    print("Case #{}: {}".format(i, calc_time(angle_1, angle_2, angle_3)))

# -----------------------------------------
# Model Solution
#
# Time  Complexity: O(3! * 60)
# Space Complexity: O(1)
# -----------------------------------------
# Ref: https://www.youtube.com/watch?v=21ADzj9dzz4
import itertools

MARK = 720 * 1e9

def calc_time(angle_1, angle_2, angle_3):
    if angle_1 == angle_2 == angle_3:
        return '0 0 0 0'

    for h, m, s in itertools.permutations([angle_1, angle_2, angle_3], 3):
        for k in range(59):
            rotate_ticks = (60 * k * MARK - 60 * m + s) / 59
            new_h = ((h + rotate_ticks) % (60 * MARK) + 60 * MARK) % (60 * MARK)
            new_m = ((m + rotate_ticks) % (60 * MARK) + 60 * MARK) % (60 * MARK)
            new_s = ((s + rotate_ticks) % (60 * MARK) + 60 * MARK) % (60 * MARK)
            if 12 * (new_h % (5 * MARK)) == new_m and 60 * (new_m % MARK) == new_s:
                output_h = new_h // (5 * MARK)
                output_m = new_m // MARK
                output_s = new_s // MARK
                output_n = (new_s % MARK) // 720
                return ' '.join([str(int(output_h)), str(int(output_m)), str(int(output_s)), str(int(output_n))])
    return '0 0 0 0'

t = int(input())
for i in range(1, t + 1):
    angle_1, angle_2, angle_3 = [int(s) for s in input().split(" ")]
    print("Case #{}: {}".format(i, calc_time(angle_1, angle_2, angle_3)))
