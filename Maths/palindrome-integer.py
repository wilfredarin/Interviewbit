def isPalindrome(self, A):
        a = list(str(A))
        n = len(a)
        Flag = 0
        for i in range(n//2):
            if a[i] != a[-(i+1)]:
                Flag = 1
                break
        if not Flag:
            return 1
        else:
            return 0
