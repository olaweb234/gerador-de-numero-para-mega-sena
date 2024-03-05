from random import randint
from time import sleep
lista=list()
jogos= list()
user = int(input('Quantos jogos você quer jogar:'))
total=1
while total<=user:

    cont=0
    while True:
        num= randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
              
        if cont >= 6:
            break   
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total+=1
print('-='*3,f'{user} jogos saindo ','-='*3)
for i,l in enumerate(jogos):
    print(f'jogos{i+1}: {l}')
    sleep(1)





