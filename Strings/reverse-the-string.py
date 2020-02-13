class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        """def solve(self, A):
        return ' '.join(A.strip().split()[::-1])
        """
        A.strip()
        A = list(A.split())
        A.reverse()
        ans=""
        for i in A:
            ans+=i+" "
        ans = ans[:-1]
        return ans
        
