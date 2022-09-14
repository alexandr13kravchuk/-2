def log(login="goodpython"):
    return login
print(log())
enter=log
print(enter())
def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
        sum_numbers([1, 2, 3, 4, 5])
        sum_numbers([])
    return total
print(sum_numbers)
sumX=sum_numbers
print(sumX)
def log(login="goodpython"):
    print("мы внутри log()")
def enter():
    return "мы внутри enter()"
def sumX(numbers):
    return "мы внутри sumX()"
print(enter())
print(sumX)
print("мы внутри log()")

def a_new_decorator(sum_numbers):
    def wrapTheFunction():
        print("Проверяет если пользовател - админ выводит сумму счета", sumX)
        a_func()
        print("Если не админ - Сумму не выводить сумму")
        return wrapTheFunction
def a_function_requiring_decoration():
    print("Проверяет если пользовател - админ выводит сумму счета", sumX)
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)



    
    




