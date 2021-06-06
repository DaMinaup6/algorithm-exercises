# -----------------------------------------
# My Solution: Binary Search + Prefix Sum
#
# Time  Complexity: O(nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# n := max(len(packages), sum(len(box) for box in boxes))
import bisect

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()

        package_prefix_sums = [0]
        for package in packages:
            package_prefix_sums.append(package_prefix_sums[-1] + package)

        def package_sum_betweeb(i, j):
            return package_prefix_sums[j + 1] - package_prefix_sums[i] if i <= j else 0

        min_space_wasted = float('inf')
        for box in boxes:
            box.sort()
            if box[-1] < packages[-1]:
                continue

            # Note: there is only one package allowed to be packed in each box
            # e.g. packages == [2, 3, 5] and box == [4, 8]
            #      for box_size == 4, use binary search to find that for packages[0] to packages[1] can be packed and record index 1 in last_packed_package_index
            #      then we can calculate the space wasted by using prefix sum of packages
            #      for box_size == 8 we will find packages[2] can be packed, calculate space wasted again and we get the total space wasted for current supplier
            last_packed_package_index = -1
            space_wasted = 0
            for box_size in box:
                package_index = bisect.bisect_left(packages, box_size, last_packed_package_index + 1)
                if package_index == len(packages) or packages[package_index] > box_size:
                    package_index -= 1
                # there might be packages with same size
                # e.g. packages == [2, 3, 3, 5] and box_size == 3
                #      will find that package_index == 1
                #      but actually we need package_index to be 2 since packages[2] can be packed in box_size 3 too
                #      so use bisect_right and we will get index 3, minus 1 to get index 2
                if packages[package_index] == box_size:
                    package_index = bisect.bisect_right(packages, box_size) - 1

                packages_space_sum = package_sum_betweeb(last_packed_package_index + 1, package_index)
                if packages_space_sum > 0:
                    space_wasted += box_size * (package_index - last_packed_package_index) - packages_space_sum

                last_packed_package_index = package_index
                if last_packed_package_index >= len(packages) - 1:
                    break

            min_space_wasted = min(min_space_wasted, space_wasted)

        return min_space_wasted % (10 ** 9 + 7) if min_space_wasted != float('inf') else -1
