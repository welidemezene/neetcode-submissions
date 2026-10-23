class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len1 = len(nums)
        len2 = len(set(nums))
        if len1 == len2:
            return False
        else:
            return True    