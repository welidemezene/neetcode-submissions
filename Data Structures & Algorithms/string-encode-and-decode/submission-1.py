class Solution:
    def encode(self, strs: List[str]) -> str:

        str1 = ""
       
        for word in strs:
            str1 += str(len(word)) + "#" + word
        return str1    




    def decode(self, s: str) -> List[str]: 
        list1 = [] 

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            len1 = int(s[i:j])
            list1.append(s[j+1 : len1 + j+1])
            i = len1 + 1 + j
        return list1        



       
       