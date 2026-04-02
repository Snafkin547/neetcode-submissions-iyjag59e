class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tempStack = []
        for token in tokens:
            if token == "+":
                tempStack.append(tempStack.pop() + tempStack.pop())
            elif token == "-":
                second, first = tempStack.pop(), tempStack.pop()
                tempStack.append(first - second)
            elif token == "*":
                second, first = tempStack.pop(), tempStack.pop()
                tempStack.append(first * second)
            elif token == "/":
                second, first = tempStack.pop(), tempStack.pop()
                tempStack.append(int(first / second))
            else:
                tempStack.append(int(token))
        
        return tempStack.pop()