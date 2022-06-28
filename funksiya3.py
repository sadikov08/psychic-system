def katta_harf(ismlar):
    for ism in range(len(ismlar)):
        ismlar[ism] = ismlar[ism].title()
    return ismlar
royxat = ["muslimbek", "sodiq", "muhsinjon",]
yangi_royxat = katta_harf(royxat[:])
katta_harf(royxat)
print(royxat)
print(yangi_royxat)
print("  ")
def bahola(ismlar1):
    baholar = {}
    for ism1 in ismlar1:
        baho = input(f"Talaba {ism1.title()}ning bahosini kiriting: ")
        baholar[ism1] = baho
    return baholar
talabalar = ["ali", "valic", "hasan", "hysan"]
baholar = bahola(talabalar)
print(baholar)
print(talabalar)
print("   ")
def kopaytmani_top(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma
print(kopaytmani_top(12,4,7))
print(" ")
def talaba_info(ism, familiya, **kwargs):
    kwargs["ism"] = ism
    kwargs["familiya"] = familiya
    return kwargs


talaba = talaba_info("Sodiqov", "Muslimbek", t_yil=2005, t_joy="Andijon", tel_raqam =1591389 )
print(talaba)