while True:
    num1 = int(input('Enter the first number: '))
    op = input('Enter the operation (  +  -  /  *  ^ )  : ')
    num2 = int(input('Enter the second number: '))
    if op == '+':
        print(num1, op, num2, '=', (num1 + num2) )

    elif op == '-':
        print(num1, op, num2, '=', (num1 - num2) )

    elif op == '*':
        print(num1, op, num2, '=', (num1 * num2))

    elif op == '/':
        if num2 != 0:
            print(num1, op, num2, '=', (num1 / num2))
        else:
            print("You can't divide by zero!")

    elif op == '^':
        print(num1, op, num2, '=', (num1 ** num2))

    else:
        print('Please check your input.')
    print('Do you want to use it again?')
    print('Yes', 'No', sep = '      ')
    a = input()
    if a == 'Yes' or a == 'YES' or a == 'yes':
        continue
    elif a == 'No' or a == 'NO' or a == 'no':
        break
    else:
        print('Unknown answer. Program closed.')
        break
