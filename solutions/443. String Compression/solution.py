class Solution:
    def compress(self, chars: List[str]) -> int:
        left, right = 1, 1
        count = 1
        while right < len(chars):
            if chars[right] != chars[right - 1]:
                chars[left - 1] = chars[right - 1]
                if count > 1:
                    print(left, left + len(str(count)))
                    chars[left:left + len(str(count))] = list(str(count))
                    left += 1
                left += len(str(count))
                count = 1
            else:
                count += 1
            right += 1
        chars[left - 1] = chars[-1]
        if count > 1:
            chars[left:left + len(str(count))] = list(str(count))
            return left + len(str(count))
        return left
