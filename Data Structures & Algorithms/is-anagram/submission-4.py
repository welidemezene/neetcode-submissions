class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        st = sorted(s)
        ts = sorted(t)
        if st == ts:
            return True
        else:
            return False
