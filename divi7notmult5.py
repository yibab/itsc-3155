def number(int):
    if int%7 == 0 and int%5 != 0:
        print(int)

myNumber = input("type number")
range = myNumber.range()
for x in range:
    number(x)