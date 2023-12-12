class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['END'] =  True
        # print(self.trie)

    def search(self, word: str) -> bool:
        def traverse(node, word: str):
            if len(word) == 0:
                return "END" in node
            if word[0] == ".":
                return any([traverse(node[i], word[1:]) for i in node.keys() if i != "END"])
            elif word[0] not in node:
                return False
            else:
                return traverse(node[word[0]], word[1:])

        return traverse(self.trie, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
