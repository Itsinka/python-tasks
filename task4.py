# Ввод текста от пользователя
text = input("Please enter text: ")

# Ввод от пользователя слова или буквы для замены
replacement = input("Please, choose a word or letter to be replaced: ")

# Замена слова или буквы в тексте на верхний регистр
modified_text = text.replace(replacement, replacement.upper())

# Вывод измененного текста
print("Modified text: ")
print(modified_text)