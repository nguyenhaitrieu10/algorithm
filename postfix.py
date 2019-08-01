
def format_string(s):
    return s.replace(" ", "")


def get_prior(c):
    if c == '+' or c == '-':
        return 1
    if c == '*' or c == '/':
        return 2
    return 0


def is_operation(c):
    if get_prior(c) == 0 and c not in ('(', ')'):
        return True
    return False


def covert_to_postfix(a):
    num = ""
    stack = []
    output = []
    for c in a:
        if is_operation(c):
            num += c
        else:
            if num != "":
                output.append(num)
                num = ""

            if c == "(":
                stack.append(c)
            elif c == ")":
                oper = stack.pop()
                while oper != "(":
                    output.append(oper)
                    oper = stack.pop()
            else:
                pior = get_prior(c)
                while len(stack) > 0 and pior <= get_prior(stack[-1]):
                    output.append(stack.pop())
                stack.append(c)

    if num != "":
        output.append(num)

    while len(stack) > 0:
        output.append(stack.pop())

    return output


def cal_postfix(postfix):
    output = []
    for c in postfix:
        if is_operation(c):
            output.append(c)
        else:
            b = output.pop()
            a = output.pop()
            result = do_calculate(a, b, c)
            output.append(result)

    return output.pop()


def do_calculate(a, b, oper):
    a = float(a)
    b = float(b)

    if oper == '-':
        return a - b
    elif oper == '+':
        return a + b
    elif oper == '*':
        return a * b
    elif oper == '/':
        return a / b


def calculate(s):
    s = format_string(s)
    postfix = covert_to_postfix(s)
    result = cal_postfix(postfix)
    return result