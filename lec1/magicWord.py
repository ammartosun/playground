import lib
import random

# word = input('give me a word: ')
# number = input('give me a number: ')

# print(f"I'm thinking of {word} {number}.")

# print("I'm thinking of " + word + " " + number + ".")

# print(type(number))
# print(word*int(number))

lib.fun()

print("Aklimdan bir sayi tuttum bil bakalim [0,10].")
num = random.randint(0,10)

bildin = False
tahmin = 0
while not bildin:
    tahmin += 1
    
    salla = input("Salla: ")
    
    if num == int(salla):
        print("Bildin cakal")
        break
    else:
        print("Bilemedin zavalli.")
        

print(f"Aferin sonunda {tahmin}. tahmininde bildin.")
