class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squares = defaultdict(set)


        for r in range(9):
            for c in range(9):

                num = board[r][c]

                if num == ".":
                    continue
                
                if num in rowSet[r] or num in colSet[c] or num in squares[(r//3, c//3)]:
                    return False
                
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
            
        return True
                
                

            

