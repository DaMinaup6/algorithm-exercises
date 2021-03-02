def threeSum(nums):
    if len(nums) <= 2:
        return []

    nums.sort()
    output = set()
    for index, num_1 in enumerate(nums[:-2]):
        if index >= 1 and num_1 == nums[index - 1]:
            continue

        temp_dict = {}
        for num_2 in nums[index + 1:]:
            if num_2 not in temp_dict:
                temp_dict[-(num_1 + num_2)] = 1
            else:
                output.add((num_1, num_2, -(num_1 + num_2)))

    return list(output) # NOTE: output is list of tuples
