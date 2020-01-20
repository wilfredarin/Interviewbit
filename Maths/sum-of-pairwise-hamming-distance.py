def hammingDistance(self, A):
        ans = 0
        for i in range(31):
            count=0
            for j in A:
                if (j&(1<<i)):
                    count+=1
                #print(A[i],A[j])
            ans+=count*(len(A)-count)*2
        return (ans)%1000000007
