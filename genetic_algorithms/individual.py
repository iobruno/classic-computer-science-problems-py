from abc import ABC, abstractmethod

import numpy as np
from numpy import ndarray
from typing import List, TypeVar, Tuple
from dataclasses import dataclass, field


T = TypeVar('T', bound='Individual')
C = TypeVar('C', bound='Chromosome')
G = TypeVar('G')


@dataclass
class Individual(ABC):
    """
    Each individual is a representation of a possible solution to the problem
    we're trying to solve.

    It should contain a set of one or more chromosomes, so long as each
    chromosome solves part of the problem
    """
    gen: int
    score: int = field(init=False)
    chromosomes: List[C]

    @abstractmethod
    def fitness(self) -> float:
        ...

    @abstractmethod
    def mutate(self, gen: int) -> T:
        ...

    @abstractmethod
    def cross_over(self, other: T, offspring_gen: int) -> Tuple[T, T]:
        ...

    def flatten_genes(self) -> ndarray:
        return np.concatenate([chromosome.genes for chromosome in self.chromosomes])


@dataclass
class Chromosome(ABC):
    """
    Represents a group (or list) of genes, defining the traits of an individual
    For this specific scenario, each Chromosome represets the route of a vehicle
    """
    score: int = field(init=False)
    genes: ndarray

    @abstractmethod
    def fitness(self) -> int:
        ...
