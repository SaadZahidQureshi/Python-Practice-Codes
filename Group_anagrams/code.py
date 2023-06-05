from collections import defaultdict



def group_anagrams(words):
    dfdict = defaultdict(list)
    for word in words:
        sort_word = ' '.join(sorted(word))
        dfdict[sort_word].append(word)
    return dfdict.values()
        
        
words_list = ["car", "tea", "eat", "bat", "ate", "arc"]
print(group_anagrams(words_list))