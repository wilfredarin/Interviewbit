#https://www.interviewbit.com/problems/possibility-of-finishing-all-courses-given-prerequisites/#
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        graph = {}
        n = len(C)
        for i in range(n):
            node = C[i]
            pre = B[i]    
            if pre in graph:
                graph[pre].append(node)
            else:
                graph[pre] = [node]
            if node not in graph:
                graph[node] = []
        def isCycle(v, visited , stack ,graph):
            visited[v] = 1
            stack[v] = 1
            for nbr in graph[v]:
                if not visited[nbr]:
                    if isCycle(nbr , visited , stack ,graph):
                        return 1
                elif stack[nbr]:
                    return 1
            stack[v] = 0
            return 0
        def cycle(n, graph):
            visited  = [0 for i in range(A+1)]
            stack = [0 for i in range(A+1)]
            for nodes in graph:
                if not visited[nodes]:
                    if isCycle(nodes, visited, stack , graph):
                        return 1
            return 0
        if cycle(n,graph):
            return 0
        else:
            return 1
                
