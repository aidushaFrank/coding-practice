# 35. Search Insert Position (LeetCode)
# Difficulty: Easy
# Learned: binary search, left/right pointers, middle index, O(log n) time complexity

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1 

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1

        return left
            
        
