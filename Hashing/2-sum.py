def twoSum(self, A, B):
        hash = {}
        for i in range(len(A)):
            if B-A[i] in hash:
                return (hash[B-A[i]]+1,i+1)
            #put it in hash if not there {}{1}
            elif A[i] not in hash:
                hash[A[i]]=i
        return []
