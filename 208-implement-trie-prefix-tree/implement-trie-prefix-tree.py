class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        # create a root node.
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        # curr pointer is seeing root at the moment.
        root = self.root
        curr = root

        for char in word:
            if char not in curr.children:
                # Create the new dict mapping our new door.
                curr.children[char] = TrieNode()
            
            # move forward traverse our prefix tree no matter what
            curr = curr.children[char]

        curr.isEndOfWord = True


    def search(self, word: str) -> bool:
        root = self.root
        curr = root

        for char in word:
            if char not in curr.children:
                return False
            else:
                # it means it's there let's move forward.
                curr = curr.children[char]
        
        # is it a word? Does it exist or does it require creation
        return curr.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        curr = root

        for char in prefix:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]

        # We have traversed our path of strings and turns out, the prefix was there
        # all along let's return True
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)