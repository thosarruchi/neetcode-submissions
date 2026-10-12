class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # find = target - nums[j]
        if len(nums) < 2: 
            return []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                find = target - nums[i]
                if nums[j] == find:
                    return [i,j]




                
        
            