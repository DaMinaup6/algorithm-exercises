# -----------------------------------------
# O(n): My Solution
# -----------------------------------------
# def product_of_array_except_self(nums):
#     zero_indexes = [index for index, num in enumerate(nums) if num == 0]
#     if len(zero_indexes) >= 2:
#         return [0 for _ in range(len(nums))]
#
#     all_products_except_zero = 1
#     for num in nums:
#         if num != 0:
#             all_products_except_zero *= num
#
#     no_zero = len(zero_indexes) == 0
#     output  = []
#     for num in nums:
#         if no_zero:
#             output.append(all_products_except_zero / num)
#         else:
#             output.append(all_products_except_zero if num == 0 else 0)
#
#     return output

# -----------------------------------------
# O(n): No Division
# -----------------------------------------
def product_of_array_except_self(nums):
    left_products  = [1 for _ in range(len(nums))]
    right_products = [1 for _ in range(len(nums))]
    for num_idx in range(1, len(nums)):
        left_products[num_idx] = nums[num_idx - 1] * left_products[num_idx - 1]
    for num_idx in range(len(nums) - 2, -1, -1):
        right_products[num_idx] = nums[num_idx + 1] * right_products[num_idx + 1]

    output = []
    for num_idx in range(len(nums)):
        output.append(left_products[num_idx] * right_products[num_idx])
    return output

print(f"product_of_array_except_self([1, 2, 3, 4])   == [24, 12, 8, 6]:    {product_of_array_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]}")
print(f"product_of_array_except_self([1, 2, 3, 0])   == [0, 0, 0, 6]:      {product_of_array_except_self([1, 2, 3, 0]) == [0, 0, 0, 6]}")
print(f"product_of_array_except_self([1, 0, 3, 0])   == [0, 0, 0, 0]:      {product_of_array_except_self([1, 0, 3, 0]) == [0, 0, 0, 0]}")
print(f"product_of_array_except_self([1, -2, -3, 6]) == [36, -18, -12, 6]: {product_of_array_except_self([1, -2, -3, 6]) == [36, -18, -12, 6]}")
