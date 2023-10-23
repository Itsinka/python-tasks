number = int(input("Please, input a number: "))

# Переводим числа в двоичную, шестнадцатеричную и восьмеричную формы
binary_number = bin(number)
hexadecimal_number = hex(number)
octal_number = oct(number)

print(f"The {number} in binary: {binary_number}, in Hexadecimal: {hexadecimal_number},  in octal: {octal_number}")