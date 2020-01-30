def solve(self, A):
        t = []
        ans = 0
        for i in range(len(A)):
            if A[i].lower() in ["a","e","i","o","u"]:
                ans+=len(A)-i
        return ans%10003
