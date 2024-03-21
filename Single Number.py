hash = set()
        for i in range(0,len(nums)):
            if len(nums) == 1:
                return nums[i]
            elif nums[i] not in hash:
                hash.add(nums[i])
            elif nums[i] in hash:
                hash.remove(nums[i])
        return hash.pop()
