yosh = int(input('Yoshingiz nechida? '))
if yosh<=4 and yosh<=60:
    price = "bepul"
elif yosh<=12:
    price = "10000 so'm"
else:
    price = "20000 so'm"

print(f"Sizga kirish {price}")


yosh1 = int(input("son kiriting"))
yosh2 = int(input("son kiriting"))
if yosh1 == yosh2:
    print(f"{yosh1} nilan {yosh2} teng")
elif yosh1 >= yosh2:
    print(f"{yosh1} katta {yosh2} dan")
elif yosh1 <= yosh2:
    print(f"{yosh1} dan {yosh2} katta")

mahsulotlar = ["olma","anor","nok","behi","gilos","qulupnay","orik","anjir","xurmo","olcha"]
menu = ["zakaz1 , zakaz2 , zakaz3, zakaz4 , zakaz5"]
zakaz1 = input("meva yozing")
zakaz2 = input("meva yozing")
zakaz3 = input("meva yozing")
zakaz4 = input("meva yozing")
zakaz5 = input("meva yozing")