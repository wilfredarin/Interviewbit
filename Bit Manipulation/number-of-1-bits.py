def numSetBits(self, A):
        count = 0
        while A > 0:
            A &= A - 1
            count += 1
        return count
