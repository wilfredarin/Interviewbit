class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        r_s =1
        c_c =-1
        ans = []
        for i in range(n):
            l = []
            r = 0
            c = i
            l.append(A[r][c])
            c_cur = i
            while c_cur>0:
                c_cur-=1
                r+=1
                l.append(A[r][c_cur])
            ans.append(l)
        for i in range(n-1):
            l = []
            r = i
            c = n
            while r<n-1:
                c-=1
                r+=1
                l.append(A[r][c])
            ans.append(l)
        return ans
