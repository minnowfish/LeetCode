class Solution:
    def isValid(self, s: str) -> bool:
            opcl = {")":"(","]":"[","}":"{"}
            stack = []
            for idx in s:
                if idx not in opcl:
                  stack.append(idx)
                  continue
                if not stack or stack[-1] != opcl[idx]:
                    return False
                stack.pop()
            return not stack
