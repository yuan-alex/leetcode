class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join(["{}#{}".format(len(i), i) for i in strs])
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        remaining = 0
        window = ""

        inside = False
        for i in range(len(s)):
            window += s[i]
            if not inside and s[i] == "#":
                remaining = int(window[:-1])
                window = ""
                inside = True
            if inside and remaining == 0 and i < len(s) - 1:
                ans.append(window)
                window = ""
                inside = False
            remaining -= 1

        return ans + [window]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
