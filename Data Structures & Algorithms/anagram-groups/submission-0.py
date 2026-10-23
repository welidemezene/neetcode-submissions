class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        list1 = []
        for n in strs:
            sorteds = "".join(sorted(n))
            freq[sorteds].append(n)
        return list(freq.values())    
        


