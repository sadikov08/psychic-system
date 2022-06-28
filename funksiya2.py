def oraliq(min,max,qadam):
    sonlar = [] 
    while min<max:
        sonlar.append(min)
        min += qadam
    return sonlar
print(oraliq(0,21,2))
print("")
def malumot_saqla(ism, familiya, t_yil, t_joy, tel_raqam ='' ,e_manzil=''):
    """Foydalanuvchi ma'lumotlarini to'playdigan funksiya"""
    malumotlar = {
            "ism" : ism,
            "familiya" : familiya,
            "t_yil" :2022- t_yil,
            "t_joy" : t_joy,
            "tel_raqam" : tel_raqam,
            "e_manzil" : e_manzil,
            }
    return malumotlar

print("Mijoz haqida ma'lumotlarni kiriting.")
mijozlar = []
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    t_yil = int(input("Tug'ilgan yili: "))
    t_joy = input("Tug'ilgan joyi: ")
    tel_raqam = input("Telefon raqami: ")
    e_manzil = input("Email: ") 
    mijozlar.append(malumot_saqla(ism, familiya, t_yil, t_joy, tel_raqam, e_manzil))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob != "ha":
        break
print("Mijozlar:")
for mijoz in mijozlar:
    print(
        f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
        f"{mijoz['t_yil']}yoshda , tel raqami: {mijoz['tel_raqam']}"
    )
print("")
def son_aniqla(x,y,z):
    """Sonlarni ichidan kattasini aniqledi"""
    if x >= y and z:
        print(f"{x} katta son")
    elif z >= x and y:
        print(f"{z} katta son")
    else:
        print(f"{y} katta son")
son_aniqla(4, 5, 2)
print("")
def aylanani_top(radius, PI=3.14):
    aylana = {
        "diametr": 2 * radius,
        "perimetr": 2 * radius * PI,
        "yuza": PI * radius ** 2,
    }
    return aylana
print(aylanani_top(34))


    