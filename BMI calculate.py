import datetime
birthYear=int(input("Введите год рождения:"))
age=datetime.datetime.now().year-birthYear
print("Ваш возвраст", age, "Лет")
a = str(input("Введите ваш пол (м\ж): "))
if a == 'м':  
    print("Мужчина")  
elif a == 'ж':  
    print("Женщина")
w = float(input("Введите вес в килограммах\n"))
h = float(input("Введите рост в сантиметрах\n"))
I = int(w/(h * 0.01)**2)
#Стандартная шкала: 14 - 45
#Diff = h-w
Begin = int(14)
End = int(45)
if I <= 14:  
    print("Займись собой, друг.")  
elif I <= 24:  
    print("Круто, ты здоров.")  
elif I <= 35:  
    print("Ты в прекрасной форме, можешь позволить себе KFC.")  
elif I <= 40:  
    print("Живёшь в маке.")
elif I <=45:
    print("Пора скидывать, чувак.")
else:  
    print("Бегом в спортзал")
print("\n")
print("Индекс на шкале BMI:")
print("|", "-" * (I - Begin+2), "|", "-" * (End-I+1), "|")
print(Begin, ">" * (I - Begin), I, ">" * (End-I), End)