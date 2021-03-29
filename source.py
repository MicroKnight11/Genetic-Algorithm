# Genetic Algorithm
# import math
from random import choices, randint
from typing import List
import numpy as np

Nilai_saham = List[int]
Kromosom = List[int]
Populasi = List[Kromosom]
pm = 0.2 # probabilitas mutasi
pc = 0.3 # probabilitas crossover
max_pop = 10

def generate_kromosom() -> Kromosom:
    return [randint(-100,100) for i in range(11)]

def hitung_harga(konstanta: Kromosom, nilai: Nilai_saham):
    # harga = f(x)=a0 + a1.y1 + a2.y2 + a3.y3 + .... + a10.y10
    # a = konstanta, y = nilai
    return sum(np.multiply(konstanta, nilai))

def hitung_nilai() -> Nilai_saham:
    # op = open, cl = close
    # nilai = (open + close) / 2
    op = [randint(0,10) for i in range(10)]
    cl = [randint(0,10) for i in range(10)]
    nilai = np.rint(np.add(op, cl)/2)
    nilai = np.insert(nilai, 0, 1)
    return nilai

def fitness(harga_saham: int, konstanta: Kromosom, nilai: Nilai_saham) :
    sigma = 1
    for i in range(10):
        y = hitung_harga()
        inv_y = harga_saham[i] - y
        sigma += np.power(inv_y, 2)
    epsilon = 1/10*(sqrt(sigma))
    return 1/epsilon


def initiate_pop(max_pop: int) -> Populasi:
    return [generate_gen() for i in range(max_pop)]


# def dekode_kromosom():

def parent_selection(Populasi: Populasi) -> Populasi:
    choices(
        Populasi=Populasi,
        weights=[fitness() for kromosom in Populasi],
        k=2
    )

def crossover(parentA: Kromosom, parentB:Kromosom, pc: float) -> Populasi:
    if p.random.random_sample() < pc:
        i = randint(1,10)
        print('titik potong', i)
        return parentA[0:i] + parentB[i:]
    else:
        return

def mutasi(kromosom: Kromosom, pm: float) -> Kromosom:
    for i in range(0,len(kromosom)):
        if np.random.random_sample() < pm:
            kromosom[i] = randint(-100,100)
    return kromosom

nilai = hitung_nilai()
a = generate_kromosom()
b = generate_kromosom()

print('a = ', a)
print('b = ', b)

kromosom_cross = crossover(a,b) 
print('crossover = ', kromosom_cross)
print('mutasi    = ', mutasi(kromosom_cross, pm))