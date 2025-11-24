class Solution(object):
    def isValidSudoku(self, board):
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                cell_value = board[i][j]
                if cell_value == '.':
                    continue
                box_index = (i // 3) * 3 + (j // 3)
                
                if cell_value in rows[i]:
                    return False  
                if cell_value in cols[j]:
                    return False  
                if cell_value in boxes[box_index]:
                    return False  

                rows[i].add(cell_value)
                cols[j].add(cell_value)
                boxes[box_index].add(cell_value)

        return True
        





        

        