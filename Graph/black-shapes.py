#https://www.interviewbit.com/problems/black-shapes/
class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        graph = []
        for row in A:
            graph.append(list(row))
        def dfs(graph,i,j,r,c,visited):
            if i<0 or i>r-1:
                return 
            if j<0 or j>c-1:
                return 
            if graph[i][j]=="O" or visited[i][j]:
                return
            visited[i][j]=True
            dfs(graph,i+1,j,r,c,visited)
            dfs(graph,i-1,j,r,c,visited)
            dfs(graph,i,j+1,r,c,visited)
            dfs(graph,i,j-1,r,c,visited)
        r = len(A)
        c = len(A[0])
        visited = [[False for i in range(c)] for j in range(r)]
        shapes = 0
        for i in range(r):
            for j in range(c):
                if graph[i][j]=="X" and not visited[i][j]:
                    dfs(graph,i,j,r,c,visited)
                    shapes+=1
        return (shapes)
                
