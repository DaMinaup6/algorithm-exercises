# -----------------------------------------
# My Solution
#
# Time  Complexity: O( 4 * math.comb(12, 4))
# Space Complexity: O(16 * math.comb(12, 4))
# -----------------------------------------
import itertools

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        
        ip_addresses = []
        for dot_positions in itertools.combinations(range(1, len(s)), 3):
            nums = [s[:dot_positions[0]], s[dot_positions[0]:dot_positions[1]], s[dot_positions[1]:dot_positions[2]], s[dot_positions[2]:]]

            ip_address_valid = True
            for num in nums:
                if int(num) < 0 or int(num) > 255 or str(int(num)) != num:
                    ip_address_valid = False
                    break
            if ip_address_valid:
                ip_addresses.append('.'.join(nums))

        return ip_addresses
