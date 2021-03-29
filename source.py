# Genetic Algorithm
import math
from random import choices
from random import randint
from typing import List
import numpy as np


nilai_saham = List[int]
Kromosom = List[int]
Population = List[Kromosom]
max_pop = 10

def generate_gen() -> Kromosom:
    return [randint(-100,100) for i in range(11)]

def hitung_harga(konstanta: Kromosom, nilai: nilai_saham):
    # harga = f(x)=a0 + a1.y1 + a2.y2 + a3.y3 + .... + a10.y10
    # a = konstanta, y = nilai
    return sum(np.multiply(konstanta, nilai))

def hitung_nilai() -> nilai_saham:
    # op = open, cl = close
    # nilai = (open + close) / 2
    op = [randint(0,10) for i in range(10)]
    cl = [randint(0,10) for i in range(10)]
    nilai = np.rint(np.add(op, cl)/2)
    nilai = np.insert(nilai, 0, 1)
    return nilai

def fitness(harga_saham: int, konstanta: Kromosom, nilai: nilai_saham) :
    sigma = 1
    for i in range(10)
        y = hitung_harga()
        inv_y = harga_saham[i] - y
        sigma += np.power(inv_y, 2)
    epsilon = 1/10*(sqrt(sigma))
    return 1/epsilon


def new_pop(max_pop: int) -> Population:
    return [generate_gen() for i in range(max_pop)]

# def dekode_kromosom():

def parent_selection(population: Population, fitness: str):
    choices(
        population,
        weights=[fitness() for kromosom in population],
        k=2
    )

# def crossover(parent):

# def mutasi():


nilai = hitung_nilai()
coba = generate_gen()

print(generate_gen())