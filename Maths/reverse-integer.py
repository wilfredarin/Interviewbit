def reverse(self, A):
        A = str(A)
        Flag = 0
        if A[0]== "-":
            A = A[1:]
            Flag = 1
        A = A[::-1]
        if Flag :
            A = int("-"+A)
        else:
            A =  int(A)
        if A > -2147483648 and A<2147483647:#2**21
            return A
        else:
            return 0
