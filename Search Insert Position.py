class Solution(object):
   def searchInsert(self, nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        # Calculate mid index properly
        m = l + (r - l) // 2
        # If the mid value is the target
        if nums[m] == target:
            return m
        elif target > nums[m]:
            l = m + 1
        else:  # target < nums[m]
            r = m - 1
    # If the target is not in the list, return the left pointer
    return l
        
