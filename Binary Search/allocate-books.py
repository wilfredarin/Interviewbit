def books(self, A, B):
        if len(A)<B:
            return -1
        def is_possible(pages):
            count = 1
            left = pages
            for i in (A):
                if i>pages:
                    return False
                left-=i
                if left<0:
                    count+=1
                    left = pages-i
            return count<=B
        l = 0
        h = sum(A)
        while l<h:
            mid = (l+h)//2
            if is_possible(mid):
                h = mid
            else:
                l = mid+1
        return l
                
