class Solution:
    def permute(self, nums):
        permutations = []

        def get_permutation(permutation, remain_nums):
            if len(remain_nums) == 0:
                permutations.append(permutation)
            else:
                for num in remain_nums:
                    get_permutation(permutation + [num], remain_nums - set([num]))
        for num in nums:
            get_permutation([num], set(nums) - set([num]))

        return permutations

processor = Solution()
print(f"processor.permute([1, 2, 3]): {processor.permute([1, 2, 3])}")
