# -----------------------------------------
# Original
# -----------------------------------------
# def getSkyline(buildings):
#     # buildings = sorted(buildings, key=lambda building: (building[0], building[1], building[2]))
#     x_list_at = { 0: [buildings[0][0], buildings[0][1]], buildings[0][2]: [buildings[0][0], buildings[0][1]] }
#     y_list_at = { buildings[0][0]: [0, buildings[0][2]], buildings[0][1]: [0, buildings[0][2]] }
#     x_ranges_at = { buildings[0][2]: [[buildings[0][0], buildings[0][1]]] }
#     left_max_height  = { buildings[0][0]: buildings[0][2] }
#     right_max_height = { buildings[0][1]: buildings[0][2] }
#
#     for building in buildings[1:]:
#         if building[2] not in x_list_at:
#             x_list_at[building[2]] = []
#         if building[0] not in y_list_at:
#             y_list_at[building[0]] = []
#         if building[1] not in y_list_at:
#             y_list_at[building[1]] = []
#         if building[2] not in x_ranges_at:
#             x_ranges_at[building[2]] = []
#         if building[0] not in left_max_height:
#             left_max_height[building[0]] = building[2]
#         if building[1] not in right_max_height:
#             right_max_height[building[1]] = building[2]
#
#         x_list_at[0]           = x_list_at[0]           + [building[0], building[1]]
#         x_list_at[building[2]] = x_list_at[building[2]] + [building[0], building[1]]
#         y_list_at[building[0]] = y_list_at[building[0]] + [0, building[2]]
#         y_list_at[building[1]] = y_list_at[building[1]] + [0, building[2]]
#         x_ranges_at[building[2]].append([building[0], building[1]])
#         left_max_height[building[0]]  = max(left_max_height[building[0]],  building[2])
#         right_max_height[building[1]] = max(right_max_height[building[1]], building[2])
#
#     x_levels = sorted(list(y_list_at.keys()))
#     y_levels = sorted(list(x_list_at.keys()))
#     key_points = [[buildings[0][0], 0]]
#     key_index  = 1
#
#     while key_points[-1] != [x_levels[-1], 0]:
#         key_point_prev = key_points[-1]
#         x_prev = key_point_prev[0]
#         y_prev = key_point_prev[1]
#         key_point = []
#
#         if key_index % 2 == 1:
#             y_list = sorted(y_list_at[x_prev])
#
#             if y_prev < y_list[-1]:
#                 key_point = [x_prev, y_list[-1]]
#             else:
#                 y_prev_idx = y_levels.index(y_prev)
#
#                 for y in y_levels[:y_prev_idx][::-1]:
#                     if y in x_ranges_at:
#                         for x_range in x_ranges_at[y]:
#                             if x_range[0] <= x_prev < x_range[1]:
#                                 key_point = [x_prev, y]
#                                 break
#                     if len(key_point) > 0:
#                         break
#                 if len(key_point) == 0:
#                     key_point = [x_prev, 0]
#         else:
#             x_prev_idx = x_levels.index(x_prev)
#
#             for x in x_levels[(x_prev_idx + 1):]:
#                 if x in left_max_height and left_max_height[x] > y_prev:
#                     key_point = [x, y_prev]
#                     break
#                 if x in right_max_height and right_max_height[x] == y_prev:
#                     extended = False
#                     if y_prev in x_ranges_at:
#                         for x_range in x_ranges_at[y_prev]:
#                             if x_range[0] <= x < x_range[1]:
#                                 extended = True
#                     if not extended:
#                         key_point = [x, y_prev]
#                         break
#                 if len(key_point) > 0:
#                     break
#             if len(key_point) == 0:
#                 x_list = sorted(x_list_at[y_prev])
#                 key_point = [x_list[-1], y_prev]
#
#         key_points.append(key_point)
#         key_index += 1
#
#     output = []
#     for idx in range(0, len(key_points)):
#         if idx % 2 == 1:
#             output.append([key_points[idx][0], key_points[idx][1]])
#     return output

# -----------------------------------------
# Priority Queue
# -----------------------------------------
def getSkyline(buildings):
    point_infos = [] # [[x, y, side_num]], where 0 means left side and 1 means right side for side_num,
    for building in buildings:
        point_infos.append([building[0], building[2], 0])
        point_infos.append([building[1], building[2], 1])
    # for left side order from highest to lowest; for right side from lowest to highest
    point_infos = sorted(point_infos, key=lambda info: (info[0], info[2], info[1] * (-1 if info[2] == 0 else 1)))

    key_points = []
    y_list = [0]
    max_val = 0
    for point_info in point_infos:
        if point_info[2] == 0:
            y_list.append(point_info[1])

            if point_info[1] > max_val:
                max_val = point_info[1]
                key_points.append([point_info[0], point_info[1]])
        else:
            y_list.remove(point_info[1])

            new_max_val = max(y_list)
            if new_max_val != max_val:
                max_val = new_max_val
                key_points.append([point_info[0], new_max_val])

    return key_points

input_01 = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
input_02 = [[0, 2, 3], [2, 5, 3]]
input_03 = [[0, 2147483647, 2147483647]]
input_04 = [[0, 2, 3], [2, 4, 3], [4, 6, 3]]
input_05 = [[1, 38, 219], [2, 19, 228], [2, 64, 106], [3, 80, 65], [3, 84, 8], [4, 12, 8], [4, 25, 14], [4, 46, 225], [4, 67, 187], [5, 36, 118], [36, 38, 230]]
input_06 = [[0, 20, 4], [1, 3, 2], [4, 5, 7], [8, 10, 10]]
input_07 = [[1, 2, 1], [1, 2, 2], [1, 2, 3]]
input_08 = [[0, 3, 3], [1, 5, 3], [2, 4, 3], [3, 7, 3]]
input_09 = [[1, 20, 1], [1, 21, 2], [1, 22, 3]]
input_10 = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3]]
input_11 = [[3, 7, 8], [3, 8, 7]]
input_12 = [[0, 5, 7], [5, 10, 7], [5, 10, 12], [10, 15, 7], [15, 20, 7], [15, 20, 12], [20, 25, 7]]
input_13 = [[16493, 367198, 110963], [31742, 366927, 405217], [37703, 87691, 651299], [41248, 869654, 436289], [51724, 170123, 202476], [53803, 865904, 443890], [54954, 57085, 742149], [78199, 232442, 96016], [87989, 822908, 511722], [91936, 370439, 843617]]
sol_01 = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
sol_02 = [[0, 3], [5, 0]]
sol_03 = [[0, 2147483647], [2147483647, 0]]
sol_04 = [[0, 3], [6, 0]]
sol_05 = [[1, 219], [2, 228], [19, 225], [36, 230], [38, 225], [46, 187], [67, 65], [80, 8], [84, 0]]
sol_06 = [[0, 4], [4, 7], [5, 4], [8, 10], [10, 4], [20, 0]]
sol_07 = [[1, 3], [2, 0]]
sol_08 = [[0, 3], [7, 0]]
sol_09 = [[1, 3], [22, 0]]
sol_10 = [[1, 3], [3, 0]]
sol_11 = [[3, 8], [7, 7], [8, 0]]
sol_12 = [[0, 7], [5, 12], [10, 7], [15, 12], [20, 7], [25, 0]]
sol_13 = [[16493, 110963], [31742, 405217], [37703, 651299], [54954, 742149], [57085, 651299], [87691, 443890], [87989, 511722], [91936, 843617], [370439, 511722], [822908, 443890], [865904, 436289], [869654, 0]]
output_01 = getSkyline(input_01); print(f"01. getSkyline(buildings_01): correct: {output_01 == sol_01}, output: {output_01}")
output_02 = getSkyline(input_02); print(f"02. getSkyline(buildings_02): correct: {output_02 == sol_02}, output: {output_02}")
output_03 = getSkyline(input_03); print(f"03. getSkyline(buildings_03): correct: {output_03 == sol_03}, output: {output_03}")
output_04 = getSkyline(input_04); print(f"04. getSkyline(buildings_04): correct: {output_04 == sol_04}, output: {output_04}")
output_05 = getSkyline(input_05); print(f"05. getSkyline(buildings_05): correct: {output_05 == sol_05}, output: {output_05}")
output_06 = getSkyline(input_06); print(f"06. getSkyline(buildings_06): correct: {output_06 == sol_06}, output: {output_06}")
output_07 = getSkyline(input_07); print(f"07. getSkyline(buildings_07): correct: {output_07 == sol_07}, output: {output_07}")
output_08 = getSkyline(input_08); print(f"08. getSkyline(buildings_08): correct: {output_08 == sol_08}, output: {output_08}")
output_09 = getSkyline(input_09); print(f"09. getSkyline(buildings_09): correct: {output_09 == sol_09}, output: {output_09}")
output_10 = getSkyline(input_10); print(f"10. getSkyline(buildings_10): correct: {output_10 == sol_10}, output: {output_10}")
output_11 = getSkyline(input_11); print(f"11. getSkyline(buildings_11): correct: {output_11 == sol_11}, output: {output_11}")
output_12 = getSkyline(input_12); print(f"12. getSkyline(buildings_12): correct: {output_12 == sol_12}, output: {output_12}")
output_13 = getSkyline(input_13); print(f"13. getSkyline(buildings_13): correct: {output_13 == sol_13}, output: {output_13}")
