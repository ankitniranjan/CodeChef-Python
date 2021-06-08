tests = int(input())

Operator = ['+', '-', '/', '*', '^', '(', ')']
Precedence = {'+':1, '-':1, '/':2, '*':2, '^':3}

def RPN(string):
    stack = []
    output = ''
    for ch in string:
        if ch not in Operator:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack[-1] != '(':
                output += stack.pop()
            stack.pop()     # pop '('
        else:
            # if there is an operator
            while stack and stack[-1] != '(' and Precedence[ch] <= Precedence[stack[-1]]:
                output += stack.pop()
            stack.append(ch)

    # Leftover
    while stack:
        output += stack.pop()
    print(output)

for _ in range(tests):
    expression = input()
    RPN(expression)
