class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows_Columns_3x3s = []

        # get rows
        for i in range(len(board)):
            rows_Columns_3x3s.append(board[i])
        
        # get columns
        for column in range(len(board)):
            columnNums = []
            for row in range(len(board)):
                columnNums.append(board[row][column])
            rows_Columns_3x3s.append(columnNums)
        
        # get 3x3s
        for row in range(0,9,3):
            for column in range(0,9,3):
                tbtNums = []
                for x in range(3):
                    for y in range(3):
                        value = board[row + x][column + y]
                        tbtNums.append(value)
                rows_Columns_3x3s.append(tbtNums)
        
        # check each list obtained
        for i in range(len(rows_Columns_3x3s)):
            onlyNums = [x for x in rows_Columns_3x3s[i] if x != "."]
            if len(onlyNums) != len(set(onlyNums)):
                return False
            for j in range(len(onlyNums)):
                if int(onlyNums[j]) > 9:
                    return False
        return True
            



        