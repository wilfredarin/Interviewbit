def findCount(self, A, B):
        n = len(A)
        l = 0
        h = n-1
        t = 0
        while l<=h:
            mid = (l+h)//2
            m = A[mid]
            if m==B:
                t = 1
                break
            elif m<B:
                l =mid+1
            else:
                h = mid-1
        if not t:
            return 0
        l = 0
        t = mid
        while t<=n-1 and A[t]==B:
            t+=1
            l+=1
        while mid>0 and A[mid-1]==B:
            mid-=1
            l+=1
        return l
