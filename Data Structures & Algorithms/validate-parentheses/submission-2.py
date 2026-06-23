class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        br_set = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        for ch in s:
            if ch in br_set.values():
                stack.append(ch)
            else:
                if stack and stack[-1] == br_set[ch]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0