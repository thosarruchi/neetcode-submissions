class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        topk = defaultdict(int) #val -> count
        for n in nums:
                topk[n] += 1
        
        heap = []
        for n in topk.keys():
            heapq.heappush(heap,(topk[n],n))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


        




            
        



        


    


        
        