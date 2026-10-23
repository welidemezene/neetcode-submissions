class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        len1 = len(nums)
        for n in nums:
            freq[n] +=1
        nums1 = sorted(freq.items(), key=lambda p:p[1] , reverse = True)    
        list1 = []
        list2 = []
        for key, value in nums1:
            list1.append(key)
        for i in range(k):
            list2.append(list1[i])
        return list2        
        
        