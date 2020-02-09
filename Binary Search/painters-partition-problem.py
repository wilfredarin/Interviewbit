def paint(self, A, B, C):
	    def is_possible(time):
	        left = time
	        count = 1
	        for i in C:
	            if time<i*B:
	                return False
                left-=i*B
                if left<0:
                    count+=1
                    left = time-i*B
            return count<=A
        l = 0
        h = sum(C)*B
        while l<h:
            mid = (l+h)//2
            if is_possible(mid):
                h = mid
            else:
                l = mid+1
        return l%10000003
