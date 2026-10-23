class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for n in nums:
            freq[n]+=1
        sor = sorted(freq.items(), key= lambda p:p[1], reverse=True)

        list1 = []
        list2 = []

        for m,l in sor:
            list1.append(m)
        for i in range(k):
            list2.append(list1[i])

        return list2        


