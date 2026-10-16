class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        i 0 1 2 3 4 5 6 7  
        n 1 7 2 5 4 7 3 6

        i 0 2 6 4 3 7 1 5
        n 1 2 3 4 5 6 7 7
        '''
        i = 0
        j = len(heights) - 1
        res = 0
        while i < j: 
            area = min(heights[i], heights[j]) * (j-i)
            res = max(res,area)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return res
         




        



        return 0 




        
         



            

        