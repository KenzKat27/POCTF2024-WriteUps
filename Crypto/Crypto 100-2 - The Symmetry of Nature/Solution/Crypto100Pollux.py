input = '84150717615789492248' + '{' + '688795176222681450_8273783252253178253147624750271202558794588687556525149_25153414179812378489258473' + '}'
output = ""
i = 0
c = input[i]
while (c != '}'):
    if (c == '0' or c == '3' or c == '6' or c == '9'):
        output = output + 'x'
    elif (c == '1' or c == '4' or c == '7'):
        output = output + '-'
    elif (c == '2' or c == '5' or c == '8'):
        output = output + '.'
    elif (c == '{' or c == '}' or c == '_'):
        output = output + c
    i = i + 1
    c = input[i]

print(output)
print(output[20])