s = "Не знаю, как там в Лондоне, я не была."\
    "Может, там собака — друг человека."\
    "А у нас управдом — друг человека!"
print(s)
#шаг 1 Количество символов
print(len(s))

#шаг 2 Развернуть строку

print(s[::-1])

#шаг 3 Сделать каждое слово с большой буквы
print(s.title())

#шаг 4 Сделать весь текст прописными буквами

print(s.upper())

#шаг 5 Найти число вхождений "нд", "ам", "о" в строку
print(s.count("нд"))
print(s.count("ам"))
print(s.count("о"))

#шаг 6 Собственные упражнения
print(s.lower())

#шаг 7 Развернуть предложение
s = "Не знаю, как там в Лондоне, я не была."\
    "Может, там собака — друг человека."\
    "А у нас управдом — друг человека!"
s = s.split()
print(s)

s = s[::-1]
print(s)

s = " ".join(s)
print(s)


#шаг 8 Вывести в консоль исходную строку
s = "Не знаю, как там в Лондоне, я не была."\
    "Может, там собака — друг человека."\
    "А у нас управдом — друг человека!"
print(s)