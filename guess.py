from random import randint
g = randint(1,100)
while True:
    n = int(input('Введи число: '))
    if g>n: print("меньше")
    elif g<n: print("больше")
    elif g==n: break
print("пабеда")