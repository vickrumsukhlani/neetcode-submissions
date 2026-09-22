class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We want to approach this with frequncy in mind

        seen = {}

        for word in strs:
            # each word gets an frequency counter
            counter = [0] * 26
                # we then loop through each char in the word and assign it to the index
            for char in word:
                # this is the index it belongs to
                index = ord(char) - ord('a') - 1
                counter[index] += 1
            
        # we create a tuple to create that as the key
        # if key not in freq dict, add the key + word, if 
            key = tuple(counter)

            if key in seen:
                seen[key].append(word)
            else:
                seen[key] = [word]
        
        result = []
        for value in seen.values():
            result.append(value)

        return result



        