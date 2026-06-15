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
                raise RuntimeError("Недостаточно операндов для выполнения операции")
            x = data.pop()
            y = data.pop()
            data.push(operations[symbol](x, y))
    if data.size() > 1:
        raise RuntimeError("Недостаточно операторов для завершения подсчета")
    return data.pop()

text = input()
print(calculate_rpn(text))