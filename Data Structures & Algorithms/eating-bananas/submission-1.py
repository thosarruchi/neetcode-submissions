class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        piles = [1,4,3,2], h = 2
        eating rate = k 
        n = len(piles)
        h = 9 hrs
        return mink
         1. sort the array = 1 2 3 4
         2. mink = piles[n-1]
         3. target == mink 
        '''
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res


