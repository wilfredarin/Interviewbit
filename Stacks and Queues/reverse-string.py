def reverseString(self, A):
        b = []
        for i in A:
            b.append(i)
        s=""
        while b:
            s+=b.pop()
        return s
