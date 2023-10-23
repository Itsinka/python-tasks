input_char = input("Please, input a character: ")

char_unicode = ord(input_char)

next_char_unicode = char_unicode + 1

# Преобразуем код Unicode следующего символа обратно в символ используя chr
next_char = chr(next_char_unicode)

print(f"The next letter is: {next_char}")

    #ord(input_char):
    # чтобы получить код Unicode введенной пользователем буквы и сохраняет его в переменной char_unicode.
    # Код Unicode - это целое число, которое представляет букву в таблице символов Unicode.

    #chr(next_char_unicode): Функция chr() преобразует код Unicode (целое число) обратно в символ.
    # Мы используем это для получения следующей буквы.

    #print(f"Следующая буква: {next_char}"): Здесь мы выводим следующую букву в алфавите, используя f-строку для форматирования строки вывода.