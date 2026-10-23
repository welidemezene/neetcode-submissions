class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       cnt = nums.count(0)

       list1 = [0] * len(nums)
       list2 = []
       mult = 1
       for n in nums:
        if n!= 0:
            mult*=n
       if cnt > 1:
        return list1
       elif cnt ==1: 
        for i in range(len(nums)):
            if cnt == 1 and nums[i] == 0:
                list1[i] = mult
        return list1  
       else:    
        for n in nums:
            if n != 0:
                list2.append(mult//n)     
                
        return list2     








        