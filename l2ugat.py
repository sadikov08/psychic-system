# car0 = {
# 	'model':'lasetti',
# 	'yili':2018,
# 	'narxi':13000
# }
# car1 = {
# 	'model':'malibu',
# 	'yili':2017,
# 	'narxi':26000
# }
# car2 = {
# 	'model':'cobalt',
# 	'yili':2022,
# 	'narxi':15000
# }
# cars = [car0, car1, car2]

# for car in cars:
# 	print(f"{car['model'].title()}, {car['yili']}. Narxi: {car['narxi']}")

# print(cars[0]['model'])

# malibus = []
# for n in range(3):
# 	new_car = {
# 		'model':'malibu',
# 		'rangi':None,
# 		'yil':2020,
# 		'korobka':'avto',
# 		'narxi':None
# 	}
# 	malibus.append(new_car)

# print(malibus)

# dasturchilar = {
# 	'ali':['html', 'css', 'python'],
# 	'vali':['html', 'css', 'js'],
# 	'hasan':['php', 'cpp']
# }

# for ism, tillar in dasturchilar.items():
# 	print(f'\n{ism}ning biladigan tillari:', end=' ')
# 	for til in tillar:
# 		print(til, end=', ')


hamkasblar = {
	'ali': {
		'familiya':'valiyev',
		'tyil':1998
	},
	'vali': {
		'familiya':'aliyev',
		'tyil':1995
	},
	'hasamn': {
		'familiya':'valiyev',
		'tyil':2000
	}
}

for ism, malumot in hamkasblar.items():
	print(f"{ism}ning ma'lumotlari")
	print(f"{malumot['familiya']}. Tug'ilgan yili: {malumot['tyil']}")