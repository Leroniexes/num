from random import randint
g = randint(1,100)
while True:
    n = int(input('Введи число: '))
    if g>n: print("меньше")
    if g<n: print("больше")
    if g==n: break
print("пабеда")