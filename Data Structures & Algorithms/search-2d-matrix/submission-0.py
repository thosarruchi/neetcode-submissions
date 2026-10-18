class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ma = []
        for row in matrix:
            for m in row:
                ma.append(m)
        l = 0
        r = len(ma) - 1
        while l <= r:
            mid = l + ((r-l) // 2)
            if ma[mid] > target:
                r -= 1
            elif ma[mid] < target:
                l += 1
            elif ma[mid] == target:
                return True
        return False
        



        