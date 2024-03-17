class Solution(object):

    def evalRPN(self, tokens):
        stack = []
        for tok in tokens:
            if tok == "+":
                stack.append(stack.pop() + stack.pop())
            elif tok == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif tok == '*':
                stack.append(stack.pop() * stack.pop())
            elif tok == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(tok))
        return stack[0]
