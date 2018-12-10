## while
numbers = [12, 32, 123, 423, 113, 3222,]
even = []
odd = []
while len(numbers) > 0:
	number = numbers.pop()
	if number % 2 == 0 :
		even.append(number)
	else:
		odd.append(number)
print even
print odd

	