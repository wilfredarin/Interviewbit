#https://www.interviewbit.com/problems/scramble-string/
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isScramble(self, A, B):
        hash_table = {}
        s1 = A
        s2 = B
        def isScramble(s1,s2):
            key = s1+s2
            if key in hash_table:
                return hash_table[key]
            else:
                if len(s1)!=len(s2):
                    hash_table[key] = False
                    return False
                n = len(s1)
                if n==0:
                    hash_table[key] = True
                    return True
                if s1==s2:
                    hash_table[key] = True
                    return True
                if sorted(s1)!=sorted(s2):
                    hash_table[key] = False
                    return False
                for i in range(1,n):
                    #abcde abcde  --> ab ab  --> cde cde 
                    if isScramble(s1[0:i],s2[0:i]) and isScramble(s1[i:],s2[i:]):
                        hash_table[key] = False
                        return True
                
                    # ab de   ---->cde abc 
                    if (isScramble(s1[0:i],s2[n-i:]) and isScramble(s1[i:],s2[0:n-i])):
                        hash_table[key] = False
                        return True
            hash_table[key] = False
            return False
        if isScramble(s1,s2):
            return(1)
        else:
            return 0







      

        
