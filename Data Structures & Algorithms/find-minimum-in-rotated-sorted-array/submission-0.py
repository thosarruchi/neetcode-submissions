class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        """
        3,4,5,6,1,2
        5 6 1 2 3 4
        6 1 2 3 4 5 

        """
        while l <= r:
            mid = l + r // 2
            note = 0
            if nums[mid] > nums[r]:
                l += 1
            elif nums[mid] < nums[r]:
                r = mid
                l = 0
            else:
                return nums[mid]






        




        