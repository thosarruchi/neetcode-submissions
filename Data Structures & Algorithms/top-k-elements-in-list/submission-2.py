class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = defaultdict(int) #val -> count
        for n in nums:
                topk[n] += 1
        return sorted(topk, key=topk.get, reverse=True)[:k]

        




            
        



        


    


        
        