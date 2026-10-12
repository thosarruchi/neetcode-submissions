class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: 
            return []
        seen = {}
        for i, n in enumerate(nums):
            find = target - n 
            if find in seen:
                return [seen[find], i]
            seen[n] = i




                
        
            