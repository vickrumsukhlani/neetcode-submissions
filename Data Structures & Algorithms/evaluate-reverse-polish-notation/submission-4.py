class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Use a stack to input the values, at the end we can check if stack is empty after looking for all operands, if it's not, we do not have a valid input return False?
        # For loop, we can create a dict with all operators, do a check each loop if 

        ops = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                operator = token
                val_1 = stack.pop()
                val_2 = stack.pop()
                match operator:
                    case "+":
                         stack.append((val_1 + val_2))
                    case "-":
                        stack.append((val_2 - val_1))
                    case "*":
                        stack.append((val_1 * val_2))
                    case "/":
                       stack.append((int(val_2 / val_1)))
            
        return stack[0]
            
        