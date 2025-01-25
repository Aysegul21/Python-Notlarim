# 1 1 2 3 5 8 13
# 1 2 3 4 5 6

a = 1
b = 1
c = 1
for i in range(1,7):
    if(i > 2):
        c = a + b
        a = b
        b = c
print(c)

