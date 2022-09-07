w = float(input("Введите вес в килограммах\n"))
h = float(input("Введите рост в сантиметрах\n"))
I = int(w/(h * 0.01)**2)
#Стандартная шкала: 14 - 45
#Diff = h-w
Begin = int(14)
End = int(45)
print("\n")
print("Индекс на шкале BMI:")
print("|", "-" * (I - Begin+2), "|", "-" * (End-I+1), "|")
print(Begin, ">" * (I - Begin), I, ">" * (End-I), End)