def findMin(self, A):
        n = len(A)
        l = 0
        h = n-1
        if A[l]<=A[h]:
            return A[l]
        while l<=h:
            mid = (l+h)//2
            m = A[mid]
            p = A[(mid-1+n)%n]
            ne = A[(mid+1)%n]
            if p>=m and ne>=m:
                return m
            if m<=A[h]:
                h = mid-1
            if m>=A[l]:
                l = mid+1
