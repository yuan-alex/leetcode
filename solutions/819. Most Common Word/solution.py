class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r"\W+", " ", paragraph).lower()
        words = [i.lower() for i in paragraph.split(" ") if i not in banned]
        counts = collections.Counter(words)
        return counts.most_common()[0][0]