class Solution:
    def isValid(self, s: str) -> bool:
        # need ds to check if value is a closer, To close this out properly, we need to pop the last item on the stack ( the last input )
        # compare them and if it's equal, we are vlaid
        # we can use the closers as the key, and then the value is the equal comparator
        
        valid_paren = {
            '{':'}',
            '(':')',
            '[':']' 
            }

        stack = []


        for char in s:
            if char in valid_paren:
                stack.append(char)
            else:
                if not stack:
                    return False
                last_value = stack.pop()
                if valid_paren[last_value] != char:
                    return False
        return not stack
        