def isPower(self, A):
        sq = int(A**.5)+1
        num = 0
        n = A
        if n==1:
            return 1
        for i in range(2,sq):
            y = 2
            num = i*i
            while num<n:
                num*=i
                y+=1
            if num==n:
                return 1
        return 0
        
        """
        
        
        def isPower(self, A):
        from math import log, sqrt
        if A==1:
            return 1
        
        for i in range(2,int(sqrt(A))+1):
            x=round(log(A,i),5)
            if x%1==0:
                return 1
                
        """
