class Solution:
    def oddString(self, words: List[str]) -> str:
        diff_groups = {}

        for word in words:
            # Iterate each word
            diff = []
            # For each word let's build it's diff array iterate over len(word) - 1
            # diff = ord(word[i + 1]) - ord(word[i])
            for i in range(len(word) - 1):
                val = ord(word[i + 1]) - ord(word[i])
                diff.append(val)
            
            key = tuple(diff)
            if key in diff_groups:
                diff_groups[key].append(word)
            else:
                diff_groups[key] = [word]

        # Iterate over our map.
        for key in diff_groups:
            # If len == 1 then we have found it
            if len(diff_groups[key]) == 1:
                # Return the word
                return diff_groups[key][0]

        