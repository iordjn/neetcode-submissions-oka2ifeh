class Solution:
    def isValid(self, s: str) -> bool:
        opened_brackets = []
        brackets = {'{':'}', '[':']', '(':')'}
        for char in s:
            
            if char in brackets.keys():
                opened_brackets.append(char)
            elif char in brackets.values():
                if len(opened_brackets) > 0:
                    last_char = opened_brackets[-1]
                    if brackets[last_char] == char:
                        opened_brackets.pop()
                    else:
                        return False
                else:
                    return False
                
        if len(opened_brackets) == 0:
            return True
        else:
            return False
                
            
            