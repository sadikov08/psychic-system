mevalar = ["olma" , "behi" , "kivi" , "anor" , "xurmo"]
print(mevalar)
mevalar.sort()
print(mevalar)
print(f"Sorted royxat: {sorted(mevalar)}")
print(f"Asl ro'yxat: {mevalar}")
sonlar = list(range(3, 10))
print(sonlar)
onliksonlar = list(range(1,11))
print(onliksonlar)
onliksonlar.sort()
print(onliksonlar)
onliksonlar.sort(reverse=True)
print(onliksonlar)
juft_sonlar = list(range(4,28,2))
print(juft_sonlar)
yigindi1 = sum(juft_sonlar)
print(yigindi1)
smallest1 = min(juft_sonlar)
print("eng kichik son {smallest1}")
bigger = max(juft_sonlar)
print("eng katta son {bigger}")
print(f"ularning ayirmasi{bigger-smallest1}" )
toq_sonlar = list(range(17, 83,2))
print(toq_sonlar)
print(f"Toq sonlar: {len(toq_sonlar)}")


