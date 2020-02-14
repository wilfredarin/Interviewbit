def removeDuplicates(self, A):
        store = 0
        prev = None
        cur = 0
        if len(A)<=1:
            return len(A)
        while cur<len(A):
            if A[cur]!=prev:
                A[store]=A[cur]
                store+=1
                prev = A[cur]
            cur+=1
        A = A[:store]
        return len(A)
