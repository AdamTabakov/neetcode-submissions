
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        # Count how many of each character we need
        count = Counter(t)

        # Count how many of each character are currently in our window
        have = Counter()

        # How many different characters we currently have enough of
        current = 0

        # How many different characters we need
        required = len(count)

        left = 0

        # Keep track of the smallest valid window
        best = float('inf')
        best_str = ""

        # Expand the window using right
        for right in range(len(s)):

            # Add the current character to our window
            have[s[right]] += 1

            # If we now have enough of this character,
            # increase current
            if s[right] in count and have[s[right]] == count[s[right]]:
                current += 1

            # If we have everything we need,
            # try shrinking the window from the left
            while current == required:

                # Check if this window is smaller than our best
                if right - left + 1 < best:
                    best = right - left + 1
                    best_str = s[left:right + 1]

                # Remove the left character
                have[s[left]] -= 1

                # If removing it means we no longer have
                # enough of that character, the window is invalid
                if s[left] in count and have[s[left]] < count[s[left]]:
                    current -= 1

                # Move left forward
                left += 1

        return best_str
