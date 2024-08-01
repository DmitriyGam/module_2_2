first = int(input('ВВедите число: '))
second = int(input('ВВедите число: '))
third = int(input('ВВедите число: '))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)