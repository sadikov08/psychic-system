savol1 = ("Yoqtirgan kitobingizni kiriting")
savol1 += ("   Agar dasturni to'xtatmoqchi bo'lsangiz 'stop' deb yozing   ")
qiymat = ""
while qiymat != "stop" :
    qiymat = input(savol1)
    if qiymat == "stop " :
        print("dastur tugadi")
kirish = True
while kirish:
    qiymat = input("Yoshingizni kiriting-----")
    if str(qiymat) == "quit" or str(qiymat) == "exit" :
        break
    if int(qiymat) <= 7:
        print("Sizga kirish 2000som")
    elif int(qiymat) <=18:
        print("sizga kirish  5000som")
    elif int(qiymat) <=65:
         print("sizga kirish 10000som")
    elif int(qiymat) >=65:
        print("sizga kirish bepul")

print("dastur tugadi ))")
    
print("Kiritilgan sonning ildizini qaytaruvchi dastur.\n")
savol = "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat =  input(savol)
    if qiymat =='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
   