#create set
        num_set = set()
        for num in range(0,len(nums)):
            num_set.add(nums[num])

    
        for i in range(len(nums) + 1):
        # If the current number is not in the set, it's missing, so return it
            if i not in num_set:
                return i
              
