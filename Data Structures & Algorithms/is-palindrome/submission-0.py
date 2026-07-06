class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum())
        s = s.lower()
        n = len(s)

        if n % 2 == 0:
            part1 = s[n//2:]
        else:
            part1 = s[n //2 + 1:]
        
        part2 = s[: n//2]
        part2 = part2[::-1]

        print(part1)
        print(part2)

        return part1 == part2
        