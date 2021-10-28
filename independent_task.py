

# 1
export = float(input("Введите экспорт :"))
imporT = float(input("Введите импорт :"))

saldo = export - imporT
if saldo >= 1:
	print("Ваш доход состовляет," + str(saldo))
else:
	print("Ваш убыток состовляет," + str(saldo)) 

#2
a = float(input("Введите число a :"))
b = float(input("Введите число b :"))
c = float(input("Введите число c :"))

if a < b < c or c < b < a:
	print("Число b среднее")
elif b < a < c or c < a < b:
	print("Число a среднее")
elif a < c < b or b < c < a:
	print("Число с среднее")
else:
	print("Ошибка, числа совпадают")

#3
a = int(input("Введите число 1 :"))
b = int(input("Введите число 2 :"))
if a % 2 == 0  and b % 2 ==0:
	print(True)
else:
	print(False)


