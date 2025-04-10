import math_utils

def main():
        x = int(input("Enter number1: "))
        y = int(input("Enter number2: "))
        operator = input("Enter operator: ").strip()

        operations = {
            '+': math_utils.add,
            '-': math_utils.subtract,
            '*': math_utils.multiply,
            '/': math_utils.divide,
            '**': math_utils.power,
            '%': math_utils.mod
        }

        if operator in operations:
            result = operations[operator](x, y)
            print("Result:", result)
        else:
            print("Invalid operator.")


if __name__ == "__main__":
    main()
