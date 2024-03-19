hash = set()
        #Loop though the array
        for i in range(0,len(nums)):
            if nums[i] in hash:
                return True
            else:
                hash.add(nums[i])

        return False
                
