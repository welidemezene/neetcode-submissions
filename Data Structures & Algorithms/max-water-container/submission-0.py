class Solution:
    def maxArea(self, heights: List[int]) -> int:
        len1 = len(heights)

        l = 0
        r = len1-1
        max1 = 0

        while l < r:
            min1 = min(heights[l],heights[r])

            lev1 = min1 * (r-l)
            if max1 < lev1:
                max1 = max(max1,lev1)
            elif heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return max1                
        