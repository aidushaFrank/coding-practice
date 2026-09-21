# 26. Remove Duplicates from Sorted Array (LeetCode)
# Difficulty: Easy
# Learned: two pointers, in-place modification, indexing, comparing adjacent unique values

class Solution(object):
    def removeDuplicates(self, nums):
        
        unique = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[unique - 1]:
                nums[unique] = nums [i]
                unique +=1
        return unique
