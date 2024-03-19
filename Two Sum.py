class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Hashmap
        map = {}
        for i in range(0 , len(nums)):
            #get the difference
            diff = target - nums[i]
            if diff in map:
                return map[diff], i
            else:
                map[nums[i]]= i
