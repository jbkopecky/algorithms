def evaluate_polish(notation):
    out = 0.
    string_operators = "*+-/"

    stack = []  # Python lists are also great stacks !

    for s in notation:
        if not s in string_operators:
            stack.append(s)
        else:
            b = stack.pop()
            a = stack.pop()
            if s == "*":
                stack.append(str(float(a) * float(b)))
            elif s == "+":
                stack.append(str(float(a) + float(b)))
            elif s == "-":
                stack.append(str(float(a) - float(b)))
            elif s == "/":
                stack.append(str(float(a) / float(b)))

    return float(stack.pop())


if __name__ == "__main__":
    polish_1 = ["2", "1", "+", "3", "*"]
    polish_2 = ["4", "13", "5", "/", "+"]
    print(evaluate_polish(polish_1))
    print(evaluate_polish(polish_2))

