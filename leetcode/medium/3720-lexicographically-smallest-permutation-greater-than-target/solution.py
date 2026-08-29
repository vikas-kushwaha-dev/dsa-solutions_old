class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)
        answer = ""

        prefix = []

        for i, ch in enumerate(target):
            # Try to make result greater at position i
            for c_ord in range(ord(ch) + 1, ord('z') + 1):
                c = chr(c_ord)
                if count[c] > 0:
                    count[c] -= 1

                    suffix = []
                    for k in range(26):
                        letter = chr(ord('a') + k)
                        suffix.append(letter * count[letter])

                    candidate = "".join(prefix) + c + "".join(suffix)
                    answer = candidate

                    count[c] += 1
                    break

            # Continue matching target exactly
            if count[ch] == 0:
                break

            count[ch] -= 1
            prefix.append(ch)

        return answer