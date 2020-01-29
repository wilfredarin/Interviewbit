def longestCommonPrefix(self, A):
        if len(A)<2:
            return A[0]
        for i in range(len(A)-1):
            j = A[i]
            k = A[i+1]
            s = ""
            o = 0
            while o<(len(j)) and o<(len(k)):
                if j[o]==k[o]:
                    s+=j[o]
                else:
                    break
                o+=1
            A[i+1]=s
        return s
