# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

n = int(input('Введите число N = '))
list = [2]
for i in range(3, n+1, 2):
	if (i > 10) and (i % 10 == 5):
		continue
	for j in list:		
		if (i % j == 0):
			break
	else:
		list.append(i)

prime_factors = []
for i in list[:int(len(list))]:
    if n % i == 0:
        prime_factors.append(i)
print(prime_factors)
