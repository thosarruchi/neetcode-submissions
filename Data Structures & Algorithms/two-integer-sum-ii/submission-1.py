class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            csum = nums[i] + nums[j]
            if csum > target:
                j -= 1
            elif csum < target:
                i += 1
            else:
                return[i+1, j+1]
        return []
            
           
            
        