
def FizzBuzz(sayi1):
    if(sayi1 % 3 == 0 and sayi1 % 5 == 0):
        print("{} sayimiz FizzBuzz sayidir".format(sayi1))

    elif(sayi1 % 3 == 0):
        print("{} sayimiz Fizz sayidir".format(sayi1))

    elif (sayi1 % 5 == 0):
        print("{} sayimiz Buzz sayidir".format(sayi1))



for i in range(1,100):
    FizzBuzz(i)













