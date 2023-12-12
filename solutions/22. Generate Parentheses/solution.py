class Solution:
    def insertAt(self, index, brackets):
        return brackets[:index] + "()" + brackets[index:]

    def generate(self, n):
        if n == 1:
            return {"()"}
        prev = self.generate(n - 1)
        new = set()
        for i in prev:
            for j in range(0, len(i) + 1):
                new.add(self.insertAt(j, i))
        return new

    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate(n)