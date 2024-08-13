class Trie:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        if word:
            cur = self.tree
            for i in range(len(word)-1):
                cur = cur.setdefault(word[i], {})
            cur[word[i+1]] = "END"

    def search(self, word: str) -> bool:
        cur = self.tree
        for i in word:
            if i not in cur:
                return False
            if cur[i] == "<END>":
                return True
            cur = cur[i]
        return False

    def startsWith(self, prefix: str) -> bool:
        result = 0
        curr = self.tree
        for i in prefix:
            if i not in curr:
                if result != 0:
                    return True
                else:
                    return False
            curr = curr[i]
            result += 1
        return False


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_3 = obj.startsWith("app")