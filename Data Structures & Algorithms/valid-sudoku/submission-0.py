from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)     # row number -> digits seen in that row
        cols = defaultdict(set)     # column number -> digits seen in that column
        boxes = defaultdict(set)    # (box-row, box-col) -> digits seen in that box

        for r in range(9):
            for c in range(9):
                d = board[r][c]             # the cell: a digit like "5", or "." if empty
                if d == ".":
                    continue                # empty: nothing to check
                box = (r//3, c//3)            # which box this cell is in
                if d in rows[r] or d in cols[c] or d in boxes[box]:
                    return False              # seen before: a duplicate
                rows[r].add(d)
                cols[c].add(d)
                boxes[box].add(d)
        return True                          # no duplicates anywhere