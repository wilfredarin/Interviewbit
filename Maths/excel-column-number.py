def titleToNumber(self, A):
        n = len(A)
        A = list(A)
        p = 0
        num = 0
        while A:
            k = A.pop()
            num += (ord(k) - 64)*((26)**p)
            p+=1
        return num
