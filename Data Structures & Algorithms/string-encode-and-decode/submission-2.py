class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ''

        for word in strs:
            encoded_str += str(len(word)) + '|' + word

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        x = 0

        while x < len(s):
            end = s.index('|', x)
            length = int(s[x:end])

            start = end + 1
            word = s[start:start + length]

            decoded_strs.append(word)

            x = start + length

        return decoded_strs