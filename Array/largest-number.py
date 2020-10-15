from functools import cmp_to_key
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def compare(self,x,y):
        if int(x+y)>int(y+x):
            return 1
        else:
            return -1
    def largestNumber(self, A):
        a = []
        for i in range(len(A)):
            a.append(str(A[i]))
        B= sorted(a,key = cmp_to_key(self.compare),reverse = True)
        while B and B[0]=="0":
            B.pop(0)
        if B:
            return "".join(B)
        return "0"
            
