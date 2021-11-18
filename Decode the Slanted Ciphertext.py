class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = int(len(encodedText) / rows)
        table = [[None for _ in range(cols)] for _ in range(rows)]
        list = []
        for x in encodedText[::-1]:
            list.append(x)
        for j in range(rows):
            for i in range(cols):
                table[j][i] = list.pop()
        text = ''
        for m in range(cols):
            for n in range(rows):
                if n+m < cols:
                    text += table[n][n+m]
        return text.rstrip()