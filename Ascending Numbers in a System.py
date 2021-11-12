class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        a = 0
        for i in s:
            if i.isdigit():
                i = int(i)
                if i > a:
                    a = i
                else:
                    return False
        return True