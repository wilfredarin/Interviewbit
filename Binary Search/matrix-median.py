def findMedian(self, A):
        n = len(A)
        m = len(A[0])
        mi = 0
        ma = 0
        for i in range(n):
            if mi>A[i][0]:
                mi = A[i][0]
            if ma<A[i][-1]:
                ma = A[i][-1]
        desired = (m*n+1)//2
        while mi<ma:
            place = [0]
            mid = mi+(ma-mi)//2
            for i in range(n):
                u = upper_bound(A[i],mid)
                place[0]+=u
            if place[0]<desired:
                mi = mid+1
            else:
                ma = mid
        return ma
