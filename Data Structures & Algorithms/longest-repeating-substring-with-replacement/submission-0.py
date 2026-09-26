class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        frequency = {}
        left = 0
        max_window = 0
        for right in range(len(s)):
            

            #frequency table
            if s[right] in frequency:
                frequency[s[right]] += 1
            else:
                frequency[s[right]] = 1
        
            #while invalid move left to right 
            
            while (right - left + 1) - max(frequency.values()) > k:
                frequency[s[left]] -= 1
                left += 1

            max_window = max(max_window, right - left + 1)
        
        return max_window
            
