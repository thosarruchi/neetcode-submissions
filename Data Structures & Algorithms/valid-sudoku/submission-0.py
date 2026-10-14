class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
            for row in board:
                values = [value for value in row if value != "."]
                if len(set(values)) != len(values):
                    return False

            # Check columns
            for col in range(9):
                values = [
                    board[row][col]
                    for row in range(9)
                    if board[row][col] != "."
                ]
                if len(set(values)) != len(values):
                    return False

            # Check 3 × 3 boxes
            for row in range(0, 9, 3):
                for col in range(0, 9, 3):
                    seen = set()

                    for r in range(row, row + 3):
                        for c in range(col, col + 3):
                            value = board[r][c]

                            if value == ".":
                                continue
                            if value in seen:
                                return False

                            seen.add(value)

            return True




        
            
                

        