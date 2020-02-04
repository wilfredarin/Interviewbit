def trailingZeroes(self, A):
        k = 5
        f = 0
        while A//k:
            f+=A//k
            k*=5
        return (f)
