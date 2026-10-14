class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(set(nums)) == 1:
            return 1

        order = sorted(set(nums))
        maxcount = 1
        count = 1
        for i in range(len(order)-1):
            if order[i+1] - order[i] == 1:
                count += 1
                if count > maxcount:
                    maxcount = count
            else:
                count = 1
                continue
        return maxcount



