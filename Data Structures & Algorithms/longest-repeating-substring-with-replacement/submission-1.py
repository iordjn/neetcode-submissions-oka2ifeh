class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        long_substring = 0
        letters = dict()
        highest_letter = None

        while right < len(s):
            highest_number = 0

            if s[right] not in letters:
                letters[s[right]] = 1
                #right += 1
            else:
                letters[s[right]] += 1
                #right += 1
            
            for letter, num in letters.items():
                if num > highest_number:
                    highest_number = num
                    highest_letter = letter

            if ((right + 1) - left) - k > highest_number:
                letters[s[left]] -= 1
                left += 1
            else:
                if long_substring < (right + 1) - (left + 0):
                    long_substring = (right + 1) - (left + 0)
            right += 1
        return long_substring
            
            

        
        