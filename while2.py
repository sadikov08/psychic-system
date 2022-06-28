print("Xarid qilmoqchi bo'lgan mahsulotlarungizni ro'yxatin i tuzamiz\n")
mahsulotlar = []
while True:
    savol = "Mahsulot nomini kiriting\n>"
    royxat = input(savol)
    mahsulotlar.append(royxat)
    savol2 = input("yana qoshasizmi ? (ha/yo'q)")
    if savol2 == "ha":
        continue
    else :
        break
    
print(mahsulotlar)

print("eBozorda harid qilmoqchi bo'lgan mahsulotlaringizni royxatini tuzamiz.")
emahsulotlar = {}
ishora = True
while ishora:
    eroyxat = input("mahsulot nomini kiriting ")
    enarx = input("Mahsulot narxini kiriting ")
    emahsulotlar[eroyxat] = int(enarx) # mahsulot kalit, narx qiymat
    javob = input("Yana harid amalga oshirmoqchimisiz? ha/yoq---")
    if javob == "ha":
        ishora = True
    else :
        ishora = False
print(emahsulotlar)

while mahsulotlar:
    mahsulot = mahsulotlar.pop()
    if mahsulot in emahsulotlar.keys():
        narh = emahsulotlar[mahsulot]
        print(f"{mahsulot.title()} - {narh} so'm")
    else:
        print(f"Bizda {mahsulot} yo'q")