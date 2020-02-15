class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        a = len(A)
        b = len(B)
        c = []
        i,j=0,0
        while i<a and j<b:
            if A[i]<B[j]:
                c.append(A[i])
                i+=1
            else:
                c.append(B[j])
                j+=1
        while i<a:
            c.append(A[i])
            i+=1
        while j<b:
            c.append(B[j])
            j+=1
        ans=""
        for i in range(a):
            ans+=str(c[i])+" "
        for i in range(a,a+b):
            ans+=str(c[i])+" "
        print(ans)
            
        
