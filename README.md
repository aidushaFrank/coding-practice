# 14. Longest Common Prefix (LeetCode)
# Difficulty: Easy
# Learned: min(..., key=len), enumerate(), nested loops, early return

class Solution(object):
    def longestCommonPrefix(self, strs):
        shortest = min(strs, key=len)
        common = ""

        for i, letter in enumerate(shortest):
            for word in strs:
                if word[i] != shortest[i]:
                    return common
            common += letter

        return common