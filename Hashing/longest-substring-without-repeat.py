"""


Given a string, 
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.

### Solution in Python ###
"""


class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        hash_map = {}
        max_len = 1
        cur_len = 1
        hash_map[A[0]]=0
        last_index = 0
        for i in range(1,len(A)):
            char = A[i]
            if (char not in hash_map) or i-cur_len>hash_map[char]:
                cur_len +=1
            else:
                max_len = max(cur_len,max_len)
                cur_len = i- hash_map[char]
            hash_map[char] = i
        max_len = max(max_len,cur_len)
        return max_len
        
                
                
                
