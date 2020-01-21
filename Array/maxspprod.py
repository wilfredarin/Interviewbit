def maxSpecialProduct(self,A):
        n = len(A)
        if n <3:
            return 0
        left = [0]*n
        right = [0]*n
        stack = []
        #right | stack has index | element's whose ryt  | min i
        #we'll find
        stack.append(0)
        for i in range(1,n):
            while stack and A[stack[-1]]<A[i]:
                #if stack less than element >> Elegible
                #pop stack | this poped element ryt is done
                right[stack.pop()] = i
            #inCase stack empty or stack ke aagey value less>>NotEligible
            stack.append(i)
        stack.clear()
        #left max i 
        stack.append(n-1)
        for i in range(n-1,-1,-1):
            #if stack less>> Eligible
            while stack and A[stack[-1]]<A[i]:
                left[stack.pop()] = i
            stack.append(i)
        m = -1
        for i in range(n):
            s = left[i]*right[i]
            m = max(s,m)
        return m
