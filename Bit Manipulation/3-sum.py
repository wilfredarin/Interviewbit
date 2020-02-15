def threeSumClosest(self, A, B):
        A.sort()
        i = 0
        m = sum(A[:3])
        #print(A)
        for i in range(len(A)-2):
            j=i+1
            k=len(A)-1
            target = B-A[i]
            while j<k-1:
                s =A[j]+A[k]
                if s==target:
                    #print("NORRRRR")
                    return (A[i]+A[j]+A[k])
                elif s<target:
                    j+=1
                else:
                    k-=1
            if abs(B-m)>abs(B-A[i]-A[j]-A[k]):
                m = A[i]+A[j]+A[k]
                #print(A[i],A[j],A[k])
        return m
