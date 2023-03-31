class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}
        for word in wordDict:
            node = trie
            for c in word:
                if c in node:
                    node = node[c]
                else:
                    node[c] = {}
                    node = node[c]
            node["END"] = True

        @lru_cache
        def startswith(word):
            if len(word) == 0:
                return True
            sol = []
            node = trie
            i = 0
            while i < len(word) and word[i] in node:
                if "END" in node:
                    sol.append(startswith(word[i:]))
                node = node[word[i]]
                i += 1
            if "END" in node:
                sol.append(startswith(word[i:]))
            return any(sol)

        return startswith(s)
