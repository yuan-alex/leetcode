class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        mapping = {")": "(", "]": "[", "}": "{"}
        history = []
        for i in s:
            if i in "({[":
                history.append(i)
            else:
                if not history or history.pop() != mapping[i]:
                    return False
        return not history