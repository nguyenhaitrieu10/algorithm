a = "abc3(qwe2(11zxc2op)zxc12qwe)"

class Enum():
    NULL = 0
    NUMBER = 1
    CHARACTER = 2
    OPEN_BRACKET = 3
    CLOSE_BRACKET = 4


def convert_postfix(a):
    l = len(a)
    i = 0
    output = []
    stack = []
    prev = Enum.NULL
    while i < l:
        # print("a[i]", a[i])
        # print("output", output)
        # print("stack", stack)
        # print("prev", prev)
        # print("-----------------")
        if a[i] == "(":
            if prev == Enum.CHARACTER or prev == Enum.CLOSE_BRACKET:
                while stack and (stack[-1] == "*" or stack[-1] == "+"):
                    output.append(stack.pop())
                stack.append("+")
            elif prev == Enum.NUMBER:
                stack.append("*")
            stack.append("(")
            i += 1
            prev = Enum.OPEN_BRACKET
            continue

        if 'a' <= a[i] <= 'z':
            if prev == Enum.NUMBER:
                stack.append("*")
            elif prev == Enum.CLOSE_BRACKET:
                while stack and (stack[-1] == "*" or stack[-1] == "+"):
                    output.append(stack.pop())
                stack.append("+")

            curStr = ""
            while i < l and 'a' <= a[i] <= 'z':
                curStr += a[i]
                i += 1
            output.append(curStr)
            prev = Enum.CHARACTER
            continue

        if '0' <= a[i] <= '9':
            if prev == Enum.CHARACTER or prev == Enum.CLOSE_BRACKET:
                while stack and (stack[-1] == "*" or stack[-1] == "+"):
                    output.append(stack.pop())
                stack.append("+")

            curNum = ""
            while i < l and '0' <= a[i] <= '9':
                curNum += a[i]
                i += 1
            output.append(int(curNum))
            prev = Enum.NUMBER
            continue

        if a[i] == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
            i += 1
            prev = Enum.CLOSE_BRACKET
            continue

        i += 1

    while stack:
        output.append(stack.pop())
    return output


postfix = convert_postfix(a)
result = []
for v in postfix:
    if v == "*" or v == "+":
        operand2 = result.pop()
        operand1 = result.pop()
        if v == "*":
            result.append(operand1*operand2)
        else:
            result.append(operand1+operand2)
    else:
        result.append(v)
    print(result)
print(result)
