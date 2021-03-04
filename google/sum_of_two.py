def sum_of_two(nums1, nums2, target):
    if len(nums1) == 0 or len(nums2) == 0:
        return False

    nums1_dict = {}
    for num in nums1:
        nums1_dict[num] = True

    for num in nums2:
        if nums1_dict.get(target - num) is True:
            return True

    return False

print(f"sum_of_two([1, 2, 3], [10, 20, 30, 40], 42) == True:  {sum_of_two([1, 2, 3], [10, 20, 30, 40], 42) == True}")
print(f"sum_of_two([1, 2, 3], [10, 20, 30, 40], 39) == False: {sum_of_two([1, 2, 3], [10, 20, 30, 40], 39) == False}")
