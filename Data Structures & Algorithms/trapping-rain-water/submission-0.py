class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        h = 0 then the water will flow so 
        unless heights[0] > heights[1] ! = 0 then lesser lena hai 
        '''
        n = len(height)
        if n == 0:
            return 0
        l = 0
        r = n - 1 
        maxl = height[l]
        maxr = height[r]
        res = 0
        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                res += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                res += maxr - height[r]
        return res

            
    

         
        
    



        