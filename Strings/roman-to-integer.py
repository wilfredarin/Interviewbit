class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        ans = 0
        R = ["I","V","X","L","C","D","M"]
        V = [1,5,10,50,100,500,1000]
        while A:
            p = A[-1]
            i = R.index(p)
            if len(A)>1:
                j = R.index(A[-2])
                if j<i:
                    ans+= V[i]-V[j]
                    A = A[:-2]
                else:
                    ans+=V[i]
                    A = A[:-1]
            else:
                ans+=V[i]
                A = A[:-1]
        return ans
