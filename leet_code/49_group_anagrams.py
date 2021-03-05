# -----------------------------------------
# My Solution
# -----------------------------------------
class Solution:
    def groupAnagrams(self, strs):
        sorted_str_dict = {}
        for str_index, string in enumerate(strs):
            sorted_str = str(sorted(string))
            if sorted_str_dict.get(sorted_str) is None:
                sorted_str_dict[sorted_str] = []

            sorted_str_dict[sorted_str].append(str_index)

        anagrams = []
        for str_indexes in sorted_str_dict.values():
            anagram = []
            for str_index in str_indexes:
                anagram.append(strs[str_index])
            anagrams.append(anagram)

        return anagrams
