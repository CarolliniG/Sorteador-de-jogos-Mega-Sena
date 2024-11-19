import random
import time
from random import randint
from time import sleep

print('-' * 40)
print(f"{'Jogando na mega sena':^30}")
print('-' * 40)
quantidade_jogos = int(input('Quantos jogos você quer? '))
jogos = []

for i in range(quantidade_jogos):
    jogo = set() # Um conjunto para garantir números únicos
    while len(jogo) < 6:
        jogo.add(random.randint(1, 60))
    jogos.append(list(jogo))

print('-=' * 3, f'SORTEANDO {quantidade_jogos} JOGOS', '-' * 3)
for i, jogo in enumerate(jogos):
    print(f'Jogo {i+1}: {sorted((jogo))}') # Ordenamos os números para melhor visualização
    time.sleep(1.5)