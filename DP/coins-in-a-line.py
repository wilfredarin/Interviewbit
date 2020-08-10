#https://www.interviewbit.com/problems/coins-in-a-line/
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        hash_table = {}
        def getBest(i,j):
            key = str(i)+"_"+str(j)
            if key in hash_table:
                return hash_table[key]
            else:
                if i==j:
                    return A[i]
                elif i + 1 == j:
                    return max(A[i],A[j])
                else:
                    # a1 [i+1 i+2...j-1 j] || [i i+1 .... j-2 j-1] aj
                    hash_table[key] =  max(A[i]+min(getBest(i+2,j),getBest(i+1,j-1)),A[j]+
                    min(getBest(i+1,j-1),
                    getBest(i,j-2)))
                    return hash_table[key]
        return getBest(0,len(A)-1)
