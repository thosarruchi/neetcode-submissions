class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ma = []
        for row in matrix:
            for m in row:
                if m == target: 
                    return True
        return False
        



        