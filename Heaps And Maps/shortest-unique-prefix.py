#https://www.interviewbit.com/problems/shortest-unique-prefix/
class Trie:
        def __init__(self):
            self.letters={}
        def addString(self,s):
            letters = self.letters
            for c in s:
                if c in letters:
                    letters[c]["freq"]+=1
                else:
                    letters[c]={"freq":1}
                letters = letters[c]
            letters["*"]=True
        def generatePrefix(self,s):
            prefix = []
            letters = self.letters
            for c in s:
                prefix.append(c)
                if letters[c]["freq"]==1:
                    break
                    
                letters = letters[c]
            return "".join(prefix)
class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        t = Trie()
        for s in A:
            t.addString(s)
        output = []
        for s in A:
            output.append(t.generatePrefix(s))
        return output
