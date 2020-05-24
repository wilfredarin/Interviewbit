#https://www.interviewbit.com/problems/valid-path/
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, A, B, C, D, E, F):
        plane = [[0]*(A+1) for i in range(B+1)]
        #check bloacked paths
        for y in range(B+1):
            for x in range(A+1):
                for c in range(C):
                    if (E[c]-x)**2+(F[c]-y)**2<=D**2:
                        plane[y][x]=-1
        #check start
    
        if plane[0][0]==-1:
            return "NO"
        plane[0][0]=1
        queue = [[0,0]]
        while queue:
            point = queue.pop(0)
            #check 8 possible location
            y = point[0]
            x = point[1]
            #left
            if x>0 and (plane[y][x-1]==0):
                plane[y][x-1]=1
                queue.append([y,x-1])
            #right
            if x<A and (plane[y][x+1]==0):
                plane[y][x+1]=1
                queue.append([y,x+1])
            #up
            if y<B and plane[y+1][x]==0:
                plane[y+1][x]=1
                queue.append([y+1,x])
            #Down
            if y>0 and (plane[y-1][x]==0):
                plane[y-1][x]=1
                queue.append([y-1,x])
            #diagLeftUP
            if x>0 and y>0 and plane[y-1][x-1]==0:
                plane[y-1][x-1]=1
                queue.append([y-1,x-1])
            #diag right up
            if x<A and y>0 and plane[y-1][x+1]==0:
                plane[y-1][x+1]=1
                queue.append([y-1,x+1])
            #diag botLeft
            if x>0 and y<B and plane[y+1][x-1]==0:
                plane[y+1][x-1]=1
                queue.append([y+1,x-1])
            #diag bot Right
            if x<A and y<B and plane[y+1][x+1]==0:
                plane[y+1][x+1]=1
                queue.append([y+1,x+1])
    
        if plane[B][A]==1:
            return "YES"
        else:
            return "NO"
            
