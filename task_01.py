# 38. Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

text = input("Введите текст ")
def del_some_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_some_words(text)
print(text)