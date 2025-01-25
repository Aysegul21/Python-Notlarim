"""#Kutuphaneler
import pandas as pd
import numpy as np
veri = pd.DataFrame({"Harf":["A","B","C","D","A","B","C","D"],"data":[1,3,4,5,8,1,2,3]})
print(veri)
print(veri.groupby("Harf").sum())

print(veri.groupby("Harf").aggregate("mean"))
data = pd.read_csv("titanic.csv")
print(data.groupby("Sex")["Age"].mean())"""

import pandas as pd
student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

print("***************************")
print(student_data)

grup = student_data.groupby("school_code").agg({"age":["mean","min","max"]})

print(grup)