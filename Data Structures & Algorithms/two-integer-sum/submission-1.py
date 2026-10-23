class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = len(nums)

        for i in range(cnt):
            for j in range(i+1,cnt):
                find = target - nums[i]
                if find == nums[j]:
                    return [i,j]
       
       