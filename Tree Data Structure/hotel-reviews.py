#https://www.interviewbit.com/problems/hotel-reviews/
class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        #create a trie
        trie = [[None] * 26, False]
        
        #add words to trie
        for good_word in A.split("_"):#wifi cool ice
            node = trie 
            for c in good_word: #w i f i, c o o l
                index = ord(c)-ord('a')
                if node[0][index] is None:
                    node[0][index] = [[None] * 26,False]
                node = node[0][index]
            node[1]=True  #end of word
        """for good_word in A.split('_'):
            node = trie
            for c in good_word:
                index = ord(c) - ord('a')
                if node[0][index] is None:
                    node[0][index] = [[None] * 26, False]
                node = node[0][index]
            node[1] = True"""
            
        reviews_score = {}
        for review_index, review in enumerate(B):
            good_words = 0
            for word in review.split('_'):
                node = trie
                for c in word:
                    index = ord(c) - ord('a')
                    node = node[0][index]
                    if node is None:
                        break
                    
                if node is not None and node[1] is True:
                    good_words += 1
            
            if good_words not in reviews_score:
                reviews_score[good_words] = []
            reviews_score[good_words].append(review_index)
            
        sorted_score = sorted(reviews_score.keys(), reverse=True)
        return [l for score in sorted_score for l in reviews_score[score]]
