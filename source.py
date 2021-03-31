# Genetic Algorithm
# import math
from random import choices, randint
from typing import List
import numpy as np
import csv
from math import sqrt

# typing
Nilai_saham = List[int]
Kromosom = List[int]
Populasi = List[Kromosom]

# global variabel
pc = 0 # probabilitas crossover
max_pop = 10
max_generation = 1000

def generate_kromosom() -> Kromosom:
    # generate [a0, a1, ..., a10]
    return [randint(-100,100) for i in range(11)]

def hitung_harga(konstanta: Kromosom, nilai: Nilai_saham):
    # f(x) = a0 + a1.y1 + a2.y2 + a3.y3 + .... + a10.y10
    # a = konstanta, y = nilai
    nilai = np.insert(nilai, 0, 1)
    return sum(np.multiply(konstanta, nilai))

def fitness_kromosom(kromosom: Kromosom, nilai: Nilai_saham, harga: int) -> float :
    y = hitung_harga(kromosom, nilai)
    return 1/(0.00000000000000000000000000000000000000000001+abs(harga - y))

# def fitness_jurnal(kromosom: Kromosom, saham: Nilai_saham) -> float:
#     sigma = 0
#     for i in range(10):
#         y = hitung_harga(kromosom,saham[i+1:i+11])
#         inv_y = saham[i] - y
#         # print('y', inv_y)
#         sigma += int(abs(inv_y ** 2))
#     # print(sigma)
#     epsilon = (1/10)*sqrt(sigma)
#     return 1/epsilon


def initiate_pop() -> Populasi:
    return [generate_kromosom() for i in range(max_pop)]

def regen_pop(populasi: Populasi, parent: Populasi) -> Populasi:
    populasi = populasi[:len(populasi)-2]
    populasi += crossover(parent[0],parent[1])
    return [mutasi(kromosom) for kromosom in populasi]

def parent_selection(populasi: Populasi, nilai: Nilai_saham, harga: int) -> Populasi:
    return choices(
        populasi,
        weights=[fitness_kromosom(kromosom, nilai, harga) for kromosom in populasi],
        k=2
    )

# def parent_selection(populasi: Populasi, saham: Nilai_saham) -> Populasi:
#     return choices(
#         populasi,
#         weights=[fitness_jurnal(kromosom, saham) for kromosom in populasi],
#         k=2
#     )

def crossover(parentA: Kromosom, parentB:Kromosom) -> tuple[Kromosom, Kromosom]:
    i = randint(1,10)
    return parentA[0:i] + parentB[i:], parentB[0:i] + parentA[i:]

def mutasi(kromosom: Kromosom) -> Kromosom:
    for i in range(0,len(kromosom)):
        if np.random.random_sample() < pm:
            kromosom[i] = randint(-100,100)
    return kromosom


#main
pop = initiate_pop()
print('initiate pop: ', pop)
pm = 1/(len(pop)*len(pop[0])) # probabilitas mutasi = 1 / banyak gen
gen = 0
saham = [1495, 1530, 1530, 1550, 1560, 1580, 1570, 1550, 1550, 1515, 1575, 1550, 1485, 1470, 1465, 1530, 1510, 1510, 1540, 1550, 1610]
harga = saham[0]
nilai = saham[1:11]
error = 0.05
while gen < max_generation: #&& !kondisi:
    gen += 1
    # sort berdasarkan fitness score
    pop = sorted(
        pop,
        # key=lambda Kromosom: fitness_jurnal(Kromosom, saham),
        key=lambda Kromosom: fitness_kromosom(Kromosom, nilai, harga),
        reverse=True
    )
    parent = parent_selection(pop, nilai, harga)
    pop = regen_pop(pop, parent)
pop = sorted(
    pop,
    # key=lambda Kromosom: fitness_jurnal(Kromosom, saham),
    key=lambda Kromosom: fitness_kromosom(Kromosom, nilai, harga),
    reverse=True
)
print('best kromosom: ', pop[0])
print('forcast harga saham: ', hitung_harga(pop[0],nilai))

