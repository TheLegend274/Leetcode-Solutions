class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set()
        set2 = set()
        set3 = set()
        
        for i in range(len(nums1)):
            if nums1[i] not in set1:
                set1.add(nums1[i])
        
        for j in range(len(nums2)):
            if nums2[j] not in set2:
                set2.add(nums2[j])
       
        # if the values in set1 and set2 are the same, add it to set 3
        for value in set1:
            if value in set2:
                set3.add(value)
        
        return set3
