class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        final = []
        hash_map = defaultdict(list)

        for word in strs:
            sorted_word =  sorted(word)
            
            hash_map[''.join(sorted_word)] += (word,)

        for value in hash_map.values():
            final.append(value)
        return final
        

        

        