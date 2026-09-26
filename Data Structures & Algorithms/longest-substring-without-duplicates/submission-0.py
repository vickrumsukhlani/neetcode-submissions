class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        curr = 0
        left = 0
        seen = set()

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                curr -= 1

            seen.add(s[right])
            curr += 1
            result = max(result, curr)


        return result