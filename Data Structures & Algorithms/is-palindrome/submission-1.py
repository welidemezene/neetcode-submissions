class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = s.lower()
        result = ""
        for c in m:
            if c.isalnum():
                result+=c
        

        dn = result[::-1]

        
        if result == dn:
            return True


            
        else:
            return False
                

                