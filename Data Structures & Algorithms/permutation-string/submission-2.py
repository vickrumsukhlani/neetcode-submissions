class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Here we can make a window, of length s1, the string we are permutating on,
        # we create a hash table with the frequency of each window slit, 
        if len(s2) < len(s1):
            return False
        s1_frequency = {}

        for char in s1:
            s1_frequency[char] = s1_frequency.get(char, 0) + 1
        

        print(s1_frequency)

        left = 0
        curr_freq = {}

        for i in range(len(s1)):
            curr_freq[s2[i]] = curr_freq.get(s2[i], 0) + 1

        print(curr_freq)

        for right in range(len(s1), len(s2)):
            if s1_frequency == curr_freq:
                return True

            curr_freq[s2[left]] -= 1
            if curr_freq[s2[left]] == 0:
                curr_freq.pop(s2[left])
            
            left += 1
            curr_freq[s2[right]] = curr_freq.get(s2[right], 0) + 1
            print(curr_freq)
        return s1_frequency == curr_freq
            