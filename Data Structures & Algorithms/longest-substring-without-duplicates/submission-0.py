class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        set1 = set()
        max1 = 0
        l = 0 
        for i in range(n):
            if s[i] not in set1:
                set1.add(s[i])
            elif s[i] in set1:
                while s[i] in set1:
                    set1.discard(s[l])
                    l+=1  
                set1.add(s[i])    
            val = i - l + 1
            if max1 < val:
                max1 = val
        return max1                  

        