from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = {} #val -> count
        ans = []
        for i,n in enumerate(nums):
            if topk.get(n):
                topk[n] += 1
            else:
                topk[n] = 1
        
        sorted_data = sorted(topk.items(), key=itemgetter(1), reverse=True)

        return [item[0] for item in sorted_data[:k]]




            
        



        


    


        
        