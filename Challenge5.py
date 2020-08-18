print('Simple calculator!')

first_number = float(input('First number? '))
if isinstance(first_number, float) == False:
    print('Please input a number.')
    exit()

operation = input('Operation? ')
if operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation !='**' and operation != '%':
    print('This is not a valid operation.')
    exit()

second_number = float(input('Second number? '))
if isinstance(second_number, float) == False:
    print('Please input a number.')
    exit()

if operation == '+':
    sum = first_number + second_number
    print(f'Sum of {first_number} {operation} {second_number} equals {round(sum, 2)}')
elif operation =='-':
    difference = first_number - second_number
    print(f'Difference of {first_number} {operation} {second_number} equals {round(difference, 2)}')
elif operation == '*':
    product = first_number * second_number
    print(f'Product of {first_number} {operation} {second_number} equals {round(product, 2)}')
elif operation == "/":
    quotient = first_number / second_number
    print(f'Quotient of {first_number} {operation} {second_number} equals {round(quotient, 2)}')
elif operation == '%':
    modulus = first_number % second_number
    print(f'Modulus of {first_number} {operation} {second_number} equals {modulus}')
else:
    exponent = first_number ** second_number
    print(f'Exponent of {first_number} {operation} {second_number} equals {exponent}')