# Genetic Algorithm
# import math
from random import choices, randint
from typing import List
import numpy as np

# typing
Nilai_saham = List[int]
Kromosom = List[int]
Harga_saham = List[int]
Populasi = List[Kromosom]

# global variabel
pm = 0.2 # probabilitas mutasi
pc = 0 # probabilitas crossover
max_pop = 10
max_generation = 10

def generate_kromosom() -> Kromosom:
    # generate [a0, a1, ..., a10]
    return [randint(-100,100) for i in range(11)]

def hitung_harga(konstanta: Kromosom, nilai: Nilai_saham):
    # harga = f(x)=a0 + a1.y1 + a2.y2 + a3.y3 + .... + a10.y10
    # a = konstanta, y = nilai
    nilai = np.insert(nilai, 0, 1)
    return sum(np.multiply(konstanta, nilai))

def hitung_nilai() -> Nilai_saham:
    # op = open, cl = close
    # nilai = (open + close) / 2
    op = [randint(0,20000) for i in range(100)]
    cl = [randint(0,20000) for i in range(100)]
    nilai = np.rint(np.add(op, cl)/2)
    return nilai

def fitness(pop: Populasi, nilai: Nilai_saham, harga: Harga_saham) :
    nilai_10 = nilai[-10:]
    fit_score = []
    for kromosom in pop:
        y = hitung_harga(kromosom, nilai_10)
        fit_score += [1/(1+abs(harga - y))]
    total = np.sum(fit_score)
    probabilitas = []
    for score in fit_score:
        probabilitas += [score/total]
    return probabilitas

# versi jurnal
#     sigma = 1
#     for i in range(10):
#         y = hitung_harga()
#         inv_y = harga_saham[i] - y
#         sigma += np.power(inv_y, 2)
#     epsilon = 1/10*(sqrt(sigma))
#     return 1/epsilon


def initiate_pop() -> Populasi:
    return [generate_kromosom() for i in range(max_pop)]

def generate_pop(parent: Populasi) -> Populasi:
    return [mutasi(crossover(parent[0],parent[1])) for i in range(max_pop)]

def parent_selection(populasi: Populasi, nilai: Nilai_saham, harga: Harga_saham) -> Populasi:
    return choices(
        populasi,
        weights=fitness(populasi, nilai, harga),
        k=2
    )

def crossover(parentA: Kromosom, parentB:Kromosom) -> Kromosom:
    # if np.random.random_sample() < pc:
    i = randint(1,10)
    # print('titik potong', i)
    return parentA[0:i] + parentB[i:]
    # else:
    #     if randint(0,1):
    #         return parentA
    #     else:
    #         return parentB 

def mutasi(kromosom: Kromosom) -> Kromosom:
    for i in range(0,len(kromosom)):
        if np.random.random_sample() < pm:
            kromosom[i] = randint(-100,100)
    return kromosom

# nilai = hitung_nilai()
# a = generate_kromosom()
# b = generate_kromosom()

# print('a = ', a)
# print('b = ', b)

# kromosom_cross = crossover(a, b) 
# print('crossover = ', kromosom_cross)
# print('mutasi    = ', mutasi(kromosom_cross))

#main
pop = initiate_pop()
gen = 1
harga = 150000
nilai = hitung_nilai()
# kondisi = 
while gen < max_generation: #&& !kondisi:
    parent = parent_selection(pop, nilai, harga)
    pop = generate_pop(parent)
    gen += 1
print('generasi: ', gen)
print('best pop: ', pop)
best_kromosom = choices(pop, weights=fitness(pop, nilai, harga), k=1)[0]
print('best kromosom: ', best_kromosom)
print('forcast saham: ', hitung_harga(best_kromosom, nilai[-10:]))