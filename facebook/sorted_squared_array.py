# -----------------------------------------
# My Solution
# -----------------------------------------
# def squared_array(nums):
#     return list(map(lambda num: num * num, nums))
#
# def merge_two_sorted_arrays(nums_1, nums_2):
#     output = []
#
#     index_1 = 0
#     index_2 = 0
#     while True:
#         if index_1 >= len(nums_1):
#             output += nums_2[index_2:]
#             break
#         if index_2 >= len(nums_2):
#             output += nums_1[index_1:]
#             break
#
#         if nums_1[index_1] < nums_2[index_2]:
#             output.append(nums_1[index_1])
#             index_1 += 1
#         else:
#             output.append(nums_2[index_2])
#             index_2 += 1
#
#     return output
#
# def sorted_squared_array(nums):
#     if nums[0] >= 0:
#         return squared_array(nums)
#     elif nums[-1] < 0:
#         return squared_array(nums)[::-1]
#     elif len(nums) == 1:
#         return [nums[0] ** 2]
#
#     non_neg_idx = -1
#     for index in range(1, len(nums)):
#         if nums[index] >= 0:
#             non_neg_idx = index
#             break
#
#     return merge_two_sorted_arrays(squared_array(nums[:non_neg_idx])[::-1], squared_array(nums[non_neg_idx:]))

# -----------------------------------------
# Two Pointers
# -----------------------------------------
def sorted_squared_array(nums):
    left_cursor  = 0
    right_cursor = len(nums) - 1

    output = []
    while left_cursor <= right_cursor:
        left_num  = nums[left_cursor]
        right_num = nums[right_cursor]
        if abs(left_num) > abs(right_num):
            output.append(left_num ** 2)
            left_cursor += 1
        else:
            output.append(right_num ** 2)
            right_cursor -= 1

    return output[::-1]

print(f"sorted_squared_array([-7, -3, -1, 4, 8, 12]) == [1, 9, 16, 49, 64, 144]: {sorted_squared_array([-7, -3, -1, 4, 8, 12]) == [1, 9, 16, 49, 64, 144]}")
print(f"sorted_squared_array([-6, -4, 1, 2, 3, 5])   == [1, 4, 9, 16, 25, 36]:   {sorted_squared_array([-6, -4, 1, 2, 3, 5]) == [1, 4, 9, 16, 25, 36]}")
print(f"sorted_squared_array([1, 2, 3])              == [1, 4, 9]:               {sorted_squared_array([1, 2, 3]) == [1, 4, 9]}")
print(f"sorted_squared_array([-3, -2, -1])           == [1, 4, 9]:               {sorted_squared_array([-3, -2, -1]) == [1, 4, 9]}")
