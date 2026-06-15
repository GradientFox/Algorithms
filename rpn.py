from stack import Stack

def calculate_rpn(notation):
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    data = Stack()
    for symbol in notation.split():
        if symbol.isnumeric():
            data.push(int(symbol))
        else:
            if data.size() < 2:
                raise ValueError("Недостаточно элементов для выполнения операции")
            x = data.pop()
            y = data.pop()
            data.push(operations[symbol](x, y))
    return data.pop()

text = input()
print(calculate_rpn(text))