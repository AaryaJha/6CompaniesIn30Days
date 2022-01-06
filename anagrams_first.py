def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        l2w=dict()
        for w in words:
            el=''.join(sorted(w))
            try:
                l2w[el].append(w)
            except:
                l2w[el]=[w]

        return list(l2w.values())