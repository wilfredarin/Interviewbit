def isPrime(self, A):
        n = A
        if n==1:
            return 0
        if n==2 :
            return 1
        for i in range(2,int(A**(.5))+1):
            if A%i==0:
                return 0
        return 1
