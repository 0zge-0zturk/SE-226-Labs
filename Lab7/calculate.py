import math_utils

def calculator():
    x = int(input("Enter a number x: "))
    y = int(input("Enter another number y: "))

    availableOperations = ['+','-','/','*','**','%']
    operatorSign = input("Enter an operator: ")

    while operatorSign not in availableOperations:
        operatorSign = input("Enter an operator: ")

    operations = {'+': math_utils.add(x,y),
                  '-': math_utils.subtract(x,y),
                  '*': math_utils.multiply(x,y),
                  '/': math_utils.divide(x,y),
                  '**': math_utils.power(x,y),
                  '%': math_utils.mod(x,y)}

    print(operations[operatorSign])

if __name__ == "__main__":
    calculator()
