from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import TypeVar

import numpy as np

T = TypeVar("T", bound="Individual")
C = TypeVar("C", bound="Chromosome")
G = TypeVar("G")


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
    chromosomes: list[C]

    @abstractmethod
    def fitness(self) -> float:
        raise NotImplementedError()

    @abstractmethod
    def mutate(self, gen: int) -> T:
        raise NotImplementedError()

    @abstractmethod
    def cross_over(self, other: T, offspring_gen: int) -> tuple[T, T]:
        raise NotImplementedError()

    def flatten_genes(self) -> np.ndarray:
        return np.concatenate([chromosome.genes for chromosome in self.chromosomes])


@dataclass
class Chromosome(ABC):
    """
    Represents a group (or list) of genes, defining the traits of an individual
    For this specific scenario, each Chromosome represets the route of a vehicle
    """

    score: int = field(init=False)
    genes: np.ndarray

    @abstractmethod
    def fitness(self) -> int:
        raise NotImplementedError()
