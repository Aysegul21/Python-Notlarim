import pandas as pd

veri = pd.DataFrame({"Info":[1,2,3,4,5,6],
                     "A":["a1","a2","a3","b1","b2","b3"]})

print(veri)
B = {
    "a1":"A",
    "a2":"A",
    "a3":"B",
    "b1":"B",
    "b2":"C",
    "b3":"C"
}
#A sutununun yanina yeni bir sutun eklenmesi
veri["Info2"] = veri["A"].map(B)
print(veri)