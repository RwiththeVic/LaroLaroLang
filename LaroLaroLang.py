import random

welcome = "Hello"
print("Pakilagay ang iyong name: ")
name = input()

print(welcome + ' ' + name)
# Number game lang ito
flag = True
while flag:
    num: str = input("Magbigay ka ng kahit anong number: ")

    if num.isdigit():
        print("Okay, arat na!")
        num = int(num)
        flag = False
    else:
        print("Number kase inde yan.... Ulitin natin")

secret = random.randint(1, num)

guess = None
count = 1

while guess != secret:
    guess = input("Okay, magbigay ka ng digits jk. number between 1 & " + str(num) + ":")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("digittt inde letter or ano paaaaaaa")
    if guess == secret:
        print("Yown tumpak mo")
    else:
        print("Hmm... ulet ka")
        count += 1

print("Ito lang naman yung tries mo,", count, "!")

