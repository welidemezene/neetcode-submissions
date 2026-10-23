class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] +=1
        list1 = []
        for key, value in freq.items():
            list1.append([key,value])
        list1.sort(key=lambda pair:pair[1])    
        res = []    
        while len(res) <k:
            res.append(list1.pop()[0])
        return res    

        