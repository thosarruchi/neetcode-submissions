class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        res = [0] * len(nums)
        count = 0
        for n in nums:
            if n != 0:
                total *= n
            else:
                count += 1
        print(total)
        print(count)
        if count > 1:
            return [0] * len(nums)
        else:
            for i,n in enumerate(nums):
                if count == 0: 
                    res[i] = total // n
                else:
                    if n == 0:
                        res = [0] * len(nums)
                        res[i] = total
        return res

        





        return []

            












                




    
        