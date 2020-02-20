def Mod(self, A, B, C):
        if A==0:
            return 0
        if B==0:
            return 1
        if B%2==0:
            y = self.Mod(A,B//2,C)
            return (y*y)%C
        else:
            y = self.Mod(A,B-1,C)
            return (y*(A%C))%C
