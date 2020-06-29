#https://www.interviewbit.com/problems/ways-to-decode/
class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        m = 10**9 +7
        if A[0] =="0":
            return 0
        else:
            n = len(A)
            count = [0 for i in range(n+1)]
            count[1] = 1
            count[0] = 1
            for i in range(2,n+1):
                count[i] = 0
                if A[i-1]>'0':
                    count[i] = count[i-1]
                if A[i-2]=="1" or (A[i-2]=='2' and A[i-1]<"7"):
                    count[i]+=count[i-2]
            return count[n]%m
                
                
