#Kutuphaneler
import pandas as pd
A_blok = pd.DataFrame({"kat":[0,1,2,3],
                       "daire":["D0","D1","D2","D3"],
                       "Oda":[1,3,4,2]})
B_blok = pd.DataFrame({"kat":[0,1,2,3],
                       "daire":["D0","D1","D2","D3"],
                       "Oda2":[3,4,5,6]})

print(A_blok)
print(B_blok)
"""
elimizde ortak olan bir sutun var ise merge kullanara birlestirebiliriz
Dikkat!! sutun ismi aynı ve degerler farkli ise farkli degerleri yazmaz 
on kullanilarak burada ortak olanlar belirtilir ise diger ortak olanlar silinmeden 
ayri bir sekilde yazilir
#******************************************
A_blok = pd.DataFrame({"kat":[0,1,2,3],
                       "daire":["D0","D1","D2","D3"],
                       "Oda":[1,3,4,2]})
B_blok = pd.DataFrame({"kat":[0,1,2,3],
                       "daire":["D0","D1","D2","D3"],
                       "Oda2":[3,4,5,6]})
print(pd.merge(A_blok,B_blok,on = "kat"))
"""
print(pd.merge(A_blok,B_blok,on = "kat"))