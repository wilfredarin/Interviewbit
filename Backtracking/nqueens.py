"""

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

N Queens: Example 1

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""

import copy
class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        
        def is_safe(board,row,col,n):
            for r in range(row):
                if board[r][col]==1:
                    return False
                    
            for c in range(col):
                if board[row][c]==1:
                    return False
            #diag
            
            for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
                if board[i][j]==1:
                    return False
            
            for i,j in zip(range(row,n,1),range(col,-1,-1)):
                if board[i][j]==1:
                    return False
            return True

        def create_board(n):
            board = [[0 for i in range(n)] for j in range(n)]
            return board
        
        def print_board(board):
            string_board = []
            for i in board:
                ans=""
                for j in i:
                    if j==1:
                        ans+="Q"
                    else:
                        ans+="."
                string_board.append(ans)
            return string_board
        
        def help_queens(board,n,col,result):
            if col>=n:
                result.append(copy.copy(print_board(board)))
            else:
                for i in range(n):
                    if is_safe(board,i,col,n):
                        board[i][col]=1
                        help_queens(board,n,col+1,result)
                        board[i][col]=0
        
        n = A
        board = create_board(n)
        result = []
        help_queens(board,n,0,result)
        return result
        
        
                    
                        
            
               

