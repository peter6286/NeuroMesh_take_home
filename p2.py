def p2(input_str):
    left = []
    output = []
    label = [' '] * len(input_str)
    
    for i, char in enumerate(input_str):
        if char == '(':
            left.append(i)
        elif char == ')':
            if left:
                left.pop()
            else:
                label[i] = '?'
    
    for i in left:
        label[i] = 'x'
    
    output.append(input_str)
    output.append(''.join(label))
    
    return '\n'.join(output)

# Sample input
test = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

for line in test :
    print(p2(line))
    print()  