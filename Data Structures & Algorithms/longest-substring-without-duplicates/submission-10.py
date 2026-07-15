class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 1

        maxLength = 0
        count = []
        
        if len(s) == 1:
            return 1
            
        while right <= len(s) - 1:
            #add the first number right away
            if len(count) == 0:
                count.append(s[left])
                # Update the max length to the length of the count list
                if len(count) > maxLength:
                    maxLength = len(count)

            

            if s[left] != s[right] and s[right] not in count:
                count.append(s[right])
                right += 1
                # Update the max length to the length of the count list
                if len(count) > maxLength:
                    maxLength = len(count)

            
            else:
                count.clear()
                left += 1
                right = left + 1
            
            
        return maxLength