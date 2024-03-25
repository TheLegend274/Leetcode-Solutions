        l = 0
        r = len(nums)-1 
        while l <= r:
            #get mid
            m = l + r /2 
            #if the mid value is the target
            if m == target:
                return  i
            elif target > m:
                l = m + 1
                return l
            elif target < m :
                r = m - 1 
                return r
        if target not in nums:
            return left
