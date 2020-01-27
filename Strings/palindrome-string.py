def isPalindrome(self, A):
        if not A:
            return 1
        s = 0
        e = len(A)-1
        while s<e:
            if A[s].isalnum() and A[e].isalnum():
                a = A[s].lower()
                b = A[e].lower()
                if a!=b:
                    return 0
                s+=1
                e-=1
            elif not A[s].isalnum():
                s+=1
            elif not A[e].isalnum():
                e-=1
        return 1
