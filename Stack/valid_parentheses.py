class Solution(object):
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in pairs:  # if char is in pairs that means it is always a closing parantheses since key in the hash map has closing parentheses only
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0


# or

# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         stack = []
#         pairs = {')':'(', ']': '[', '}':'{'}
#         for char in s:
#             if char in pairs:
#                 if stack and stack[-1] == pairs[char]:
#                     stack.pop()
#                 else:
#                     return False
#             else: 
#                 stack.append(char)
#         return True if not stack else False
        