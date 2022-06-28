avtolar = ['audi','bmw','volvo','kia','hyundai', 'gm']
for avto in avtolar:
    if avto == 'gm': 
        print(avto.upper()) 
    else: 
        print(avto.title())
        
ism = input('Ismignizni yozing----') 
if ism.lower() != 'admin': 
    print(f"Xush kelibsiz {ism} ")
else:
    print(" Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")

son = float(input("son kiriting---"))
son2 = float(input("son kiriting---"))
if son!=son2:
    print("sonlar teng emas")
else:
    print("sonlar teng")

sonn = float(input("istalgan son kirit<<<<"))
if sonn>=0:
    print("son musbat")
else:
    print("son manfiy")

son5 = float(input("sonni kirirting"))
if son5>=0:
    print(f"{son5**(1/2)}")
else:
    print("musbat son kirirting")
    def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
        """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
        mijoz = {
            "ism": ism,
            "familiya": familiya,
            "tyil": tyil,
            "yoshi": 2020 - tyil,
            "tjoy": tjoy,
            "email": email,
            "telefon": tel,
        }
        return mijoz


    print("Mijoz haqida ma'lumotlarni kiriting.")
    mijozlar = []
    while True:
        ism = input("Ismi: ")
        familiya = input("Familiyasi: ")
        tyil = int(input("Tug'ilgan yili: "))
        tjoy = input("Tug'ilgan joyi: ")
        email = input("Email: ")
        telefon = input("Telefon raqami: ")
        mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
        javob = input("Davom etasizmi? (ha/yo'q)")
        if javob != "ha":
            break

    print("Mijozlar:")
    for mijoz in mijozlar:
        print(
            f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
            f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}"
        )
