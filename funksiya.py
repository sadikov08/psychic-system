def yosh_hisobla(tugilgan_yil, joriy_yil=2022):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
tyil = int(input("Tug'ilgan yilingizni kiriting: ")) #inputni int ga o'zgartirish
yosh_hisobla(tyil)

def yosh_hisobla(tugilgan_yil, joriy_yil):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

yosh_hisobla(1993,2022) #2ci argumentni qo'yish kerak edi

def salom_ber(ism): #qiymat berilmagan edi
    """Salom beruvchi funksiya"""
    print(f"Assalomu alaykum! {ism}")

salom_ber('hasan')
def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
 
toliq_ism("olim","hasan") 
print("  ")
def son_kvadrat(kv_son):
    """Foydalanuvchidan son sorab uni kvadratini chiqaruvchi funksiya"""
    print(f"sonning kvadrati {kv_son * kv_son}ga teng \n"
          f"kubi esa {kv_son * kv_son * kv_son}ga teng")

n_son = int(input("son kiriting :  "))
son_kvadrat(n_son)
print("  ")
def son_aniqla(musb_son):
    """Sonni musbat yoki manfiy ekanini aniqlaydigan funksiya"""
    if musb_son <=0:
        print("Son manfiy")
    else:
        print("Son musbat")
manf_son = int(input("istagan soningizni kiriting :  "))
son_aniqla(manf_son)
print("  ")
def katta_son_aniqla(num,numb):
    """2ta sondan kattasini aniqlaydigan funksiya"""
    if num >=numb:
        print(f"{num} katta son")
    else:
        print(f"{numb} katta son")
mun = int(input("1-sonni kiriting :  "))
bmun = int(input("2-sonni kiriting :  "))
katta_son_aniqla(mun, bmun)
print("  ")
def daraja_kotar(x, y):
    """x ni y-darajasini ko'rsatuvchi funksiya"""
    print(f"{x}ning {y}darajasi {x**y} ga teng")
daraja_kotar(3, 4)
print('   ')
def daraja_kotar2(x, y=2):
    """x ni y-darajasini ko'rsatuvchi funksiya"""
    print(f"{x}ning {y}darajasi {x**y} ga teng")
daraja_kotar2(3)
print("   ")
def bolinuvchi(bolinma):
    for boluvchi in range(2, 11):
        if not bolinma % boluvchi:
            print(f"{bolinma} {boluvchi} ga qoldiqsiz bo'linadi")

son = int(input("son kiriting :  "))
bolinuvchi(son)
