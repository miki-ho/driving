country = input('your contry:')
age = input('your age:')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('you can drive')
	else:
		print('you cannot drive')
elif country == 'USA':
	if age >= 16:
		print('you can drive')
	else:
		print('you cannot drive')
else:
	print('only Taiwan/USA')

