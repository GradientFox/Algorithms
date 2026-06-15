from stack import Stack

OPEN_BRACKETS = ['{', '[', '(']
REFORM = {
    '}': '{',
    ']': '[',
    ')': '('
}
def check_sequence(sequence):
    data = Stack()
    for bracket in sequence:
        if bracket in OPEN_BRACKETS:
            data.push(bracket)
        else:
            if data.pop() != REFORM[bracket]:
                return "Неверная последовательность"
    if not data.is_empty():
        return "Неверная последовательность"
    return "Последовательность верная"

text = input()
print(check_sequence(text))