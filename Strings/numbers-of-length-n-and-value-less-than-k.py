def lengthOfLastWord(self, A):
        A = A.split(" ")
        A = list(A)
        while A and A[-1]=="":
            A.pop()
        if A:
            return len(A[-1])
        return 0
