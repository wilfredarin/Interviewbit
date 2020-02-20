class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        hash_map ={}
        for index in range(len(A)):
            g = list(A[index])
            g.sort()
        
            ans=""
            for i in g:
                ans+=i
            if ans in hash_map:
                hash_map[ans].append(index+1)
            else:
                hash_map[ans]=[index+1]
        res = []
        for word in hash_map.values():
            res.append(word)
        return res
            
            
