
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:54:08 2022

@author: USER
"""


mahsulotlar = ["olma" , "Behi" , "pishloq" , "non" , "sut" , "tvorog" , "qatiq" , "qaymoq"]
print(mahsulotlar)
xaridlar = []
xaridlar.append ("behi")
xaridlar.append ("sut")
xaridlar.append("qatiq")
xaridlar.append ("tvorog")
print(xaridlar)
sotuvda_yoq = []
sotuvda_yoq.append(xaridlar.pop(0))
sotuvda_yoq.append ((xaridlar.pop(2))
print(sotuvda_yoq)
mahsulotlar.remove("tvorog")
mahsulotlar.remove("sut")
print(sotuvda_yoq)
del mahsulotlar[2]
print(mahsulotlar)
