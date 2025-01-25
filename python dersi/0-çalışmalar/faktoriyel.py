sayi = int(input("faktoriyeli alinacak sayiyi giriniz:"))
fact = 1
for x in range(1,sayi+1):
    fact *= x

print(fact)
