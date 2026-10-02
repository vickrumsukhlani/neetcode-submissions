class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # since it's contigous, we have a window of ACCEPTABLE answers.
        # we need to make a left and right ptr

        # we want an iteratable hash table so that can do O(1) lookup times to check if a value is in the table
        # we can use a set
        # WINDOW: its expanding off of the start and moving right, we EXPAND when the RIGHT index
        # is NOT in the set, bc its a substring, if IT IS, we condense the left ptr and increment it right

        # we want to start at 0 and 1, 
        seen = set()
        left = 0
        curr = 0
        longest = 0

        (2)
        for right in range(len(s)):
            while(s[right] in seen): # means that we have a duplicate so move our window right
                seen.remove(s[left])
                left += 1
                curr -= 1
            
            seen.add(s[right])
            curr += 1
            longest = max(longest, curr)
        
        return longest















        # # brute force
        # longest = 0

        # for i in range(len(s)):
        #     seen = set()
        #     curr = 0
        #     for j in range(i, len(s)):
        #         if s[j] in seen:
        #             break
        #         else:
        #             seen.add(s[j])
        #             curr += 1
        #     # if we leave the check in the if statement, Consider "ABC" we never break, so we never calc longest
        #     longest = max(curr, longest) 
        # return longest