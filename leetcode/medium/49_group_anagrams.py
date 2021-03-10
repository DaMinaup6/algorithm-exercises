# -----------------------------------------
# O(N * Klog(K)): My Solution
# -----------------------------------------
# K := len(max(string for string in strs))
class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        for string in strs:
            anagram = str(sorted(string))
            if anagrams.get(anagram) is None:
                anagrams[anagram] = []

            anagrams[anagram].append(string)

        return anagrams.values()

# -----------------------------------------
# O(N * K): Categorize by Count
# -----------------------------------------
# K := len(max(string for string in strs))
class Solution:
    def str_alphabet_counts(self, string):
        alphabet_counts = [0 for _ in range(26)]
        for char in string:
            alphabet_counts[ord(char) - 97] += 1

        return alphabet_counts

    def groupAnagrams(self, strs):
        # this only applied to string with only alphabet letters
        anagrams = {}
        for string in strs:
            anagram = str(self.str_alphabet_counts(string))
            if anagrams.get(anagram) is None:
                anagrams[anagram] = []

            anagrams[anagram].append(string)

        return anagrams.values()
