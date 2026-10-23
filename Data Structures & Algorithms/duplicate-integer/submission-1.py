class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = set(nums)
        nums_length = len(nums)
        uniq_length = len(uniq)
        if nums_length > uniq_length:
            return True
        else:
            return False    

        