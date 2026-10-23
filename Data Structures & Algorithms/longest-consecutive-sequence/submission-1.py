class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num = set(nums)
        best = 0
        for x in num:
            if x-1 not in num:
                y = x
                while y + 1 in num:
                    y+=1
                best = max(best, y-x +1)
        return best            