 def prevSmaller(self, A):
        stack = [A[0]]
        b = [0]*len(A)
        b[0] =-1
        for i in range(1,len(A)):
            while stack and stack[-1]>=A[i]:
                stack.pop()
            if stack:
                b[i]=stack[-1]
                stack.append(A[i])
            elif not stack:
                b[i]=-1
                stack.append(A[i])
        return b
