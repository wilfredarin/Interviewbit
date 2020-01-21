def getRow(self, A):
        k = [1]
        if A==0:
            return k
        n = math.factorial(A)
        for i in range(1,A):
            b = n//(math.factorial(i)*(math.factorial(A-i)))
            k.append(b)
        k.append(1)
        return k
