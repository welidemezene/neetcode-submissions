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
                length = int(s[i:j])
                list1.append(s[j+1: j + 1 + length])
                i = j + 1 + length
        return list1        








       