# calculator program

def calculator():
    num1 = float(input('Enter the first operand: '))
    operator = input('Enter the operator: ')
    num2 = float(input('Enter the second operand:'))

    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                result = ''
                print('Zero division error')
            else:
                result = num1 / num2
        else:
            print('Invalid operator')
        
    except:
        print('Invalid input')

    return print(result)


if __name__ ==  "__main__":
    calculator()

