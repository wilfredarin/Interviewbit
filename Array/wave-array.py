def wave(self, A):
        A.sort()
        i = 0
        while i<(len(A)-1):
            j = i+1
            A[i],A[j]=A[j],A[i]
            i+=2
        return A
