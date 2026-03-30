class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        if len(t) != len(s):
            return False

        for letter in s:
            hash_map[letter] = s.count(letter)

        for letter in t:
            if letter in hash_map:
                hash_map[letter] -= 1
            else:
                return False

        for value in hash_map.values():
            if value !=0:
                return False
        return True
            