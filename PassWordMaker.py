import string
from random import *
print("PassWord Maker")
print("---------------")
print("Coded By Javad-Fard")
print("---------------")

print("1.Make a Password with Character and Digit (Hard)")
print("2.Make a Password with Character and Punctuation (Very Hard)")
print("3.Make a Password with Blind Signs (Insane)")
print("")
while True:
    get_num = input("Choose a Number :")
    if get_num in ["1","2","3"]:
        if get_num == "1":
            char = string.ascii_letters + string.digits
            password = "".join(choice(char) for x in range(randint(8, 16)))
            print(password)

        elif get_num == "2":
                char = string.punctuation + string.digits
                password = "".join(choice(char) for x in range(randint(8, 16)))
                print(password)

        elif get_num == "3":
                char = string.ascii_letters + string.punctuation + string.digits
                password = "".join(choice(char) for x in range(randint(8, 16)))
                print(password)

    else:
        print("Oops You Were Wrong !")
        print("Try Again")
        continue


