class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowhash = defaultdict(set)
        colhash = defaultdict(set)
        gridhash = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                else:
                    key = (r//3, c//3)
                    value = board[r][c]
                    if value in rowhash[r] or value in colhash[c] or value in gridhash[key]:
                        return False
                    rowhash[r].add(value)
                    colhash[c].add(value)
                    gridhash[key].add(value)
        return True

                





                

        