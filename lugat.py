otam = {'ismi':'Muhsinjon' , 't_yili' : '1965','millati': 'ozbek'}
print(f"otamning ismi  {otam['ismi']} \
      {otam['t_yili']}-yilda tugilgan, \
      millati  {otam['millati']}")

oila = {'buvim':'manti','otam':'osh','oyim':'lagmon','akam':'shorva','singlim':'chuchvara'}

print(f"Buvimning sevimli taomi {oila['buvim']},\
      Otamning sevimli taomi {oila['otam']},\
          Onamning sevimli taomi {oila['oyim']},\
    akamning sevimli taomi {oila['akam']},\
        Singlimning sevimli taomi {oila['singlim']}")
        
python = {'integer':'butun sonlar','float':'onlik sonlar','string':'matnlar','input':'foydalanuvchidan malumot olishda ishlatiladi','sort':'royxatni alifbo boyicha tartiblaydi','reverse':'royxatni boshini oxiriga qilishda qollanadi','sorted':'royxatni ozgarmagan holda tartiblaydi','inheritance':'meros olishda ishlatiladi','konstanta':'ozgarmas ozgaruvchi','or':'ikki va undan kop amallarni biri bajarilishini tekshirishda ishlatilinadi'}
sozlar =  input("so'z kiriting---")
if sozlar in python:
    print(python[sozlar])
else:
    print("Bunday so'z mavjud emas")