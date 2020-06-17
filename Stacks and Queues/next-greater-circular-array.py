#https://www.interviewbit.com/problems/next-greater-circular-array/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        stack = []
        ans = [-1]*n
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=A[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
                stack.append(A[i])
            else:
                ans[i]=-1
                stack.append(A[i])
        for i in range(n-1,-1,-1):
            if ans[i]==-1:
                while stack and stack[-1]<=A[i]:
                    stack.pop()
                if stack:
                    ans[i] = stack[-1]
                    stack.append(A[i])
                else:
                    ans[i]=-1
                    stack.append(A[i])
        return ans
                
                
            
                        
                
        #18 35
        #35 -1
