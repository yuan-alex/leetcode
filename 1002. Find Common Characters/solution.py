class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return [list(words[0])]
        finalResult = collections.Counter(words[0])
        for word in words[1:]:
            counts = collections.Counter(word)
            for char in counts.keys():
                if char in finalResult:
                    finalResult[char] = min(finalResult[char], counts[char])
            finalResult = {
                key: val for key, val in finalResult.items() if key in counts
            }
        output = []
        for key in finalResult:
            for i in range(0, finalResult[key]):
                output.append(key)
        return output