def solve(self, A):
        A.sort()
        p = None
        j = len(A)-1
        while j>=0:
            if A[j]!=p:
                p = A[j]
                if len(A)-j-1==A[j]:
                    return 1
            j-=1
        return -1
