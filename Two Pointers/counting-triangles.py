#https://www.interviewbit.com/problems/counting-triangles/
class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        A.sort(reverse =True)
        ans = 0
        n = len(A)
        for i in range(n-2):
            j = i+1
            k = n-1
            #if the largest size is zero ! get out man
            if A[i]==0:
                break
            while j<k:
                if A[i]<A[j]+A[k]:
                    ans+=k-j
                    j+=1
                else:
                    k-=1
        return ans%(10**9+7)
            
