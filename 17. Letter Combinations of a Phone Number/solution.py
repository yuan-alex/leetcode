class Solution:
    mappings = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def traverse(self, digits):
        digit = digits[0]
        if len(digits) == 1:
            return set(self.mappings[digit])
        prev = self.traverse(digits[1:])
        new = set()
        for i in prev:
            for j in self.mappings[digit]:
                new.add(j + i)
        return new

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        return self.traverse(digits)