class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len1 = len(s)
        len2 = len(t)
        if len2 > len1:
            return ""

        need = Counter(t)
        missing = len2
        l = 0
        
        left, right = 0,float('inf')

        for i in range(len1):
            if need[s[i]] > 0:
                missing -=1
            need[s[i]]-=1
            while missing == 0:
                need[s[l]] +=1
                if need[s[l]] > 0:
                    missing +=1
                
                if i - l + 1 < right:
                    left,right = l, i-l+1  
                l+=1        
        if right == float('inf'):
            return ""
        else:
            return s[left:right+left]    

        