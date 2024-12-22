a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
operation = input("Введіть математичну дію (+, -, *, /): ")

if operation == "+":
    print(f"Результат: {a + b}")
elif operation == "-":
    print(f"Результат: {a - b}")
elif operation == "*":
    print(f"Результат: {a * b}")
elif operation == "/":
    if b == 0:
        print("Ділення на нуль!")
    else:
        print(f"Результат: {a / b}")
else:
    print("Невідома дія.")