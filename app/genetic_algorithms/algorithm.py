from typing import TypeVar

import numpy as np
from rich.progress import track

T = TypeVar("T", bound="Individual")
C = TypeVar("C", bound="Chromosome")


class GeneticAlgorithm:
    initial_population: list[T]
    mutation_rate: float
    crossover_rate: float
    tragedy_rate: float

    def __init__(
        self,
        initial_population: list,
        mutation_rate: float,
        crossover_rate: float,
        tragedy_rate: float,
        tragedy_on_every_nth_generation: int,
        top_n: int = 1000,
    ):
        self.initial_population = initial_population
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.tragedy_rate = tragedy_rate
        self.tragedy_on_every_nth_generation = tragedy_on_every_nth_generation
        self.top_n = top_n

    def _generate_mutons(self, population: list[T], generation: int) -> list[T]:
        sample_size = int(len(population) * self.mutation_rate)
        sample = np.random.choice(population, size=sample_size)
        mutated_individual = [individual.mutate(gen=generation) for individual in sample]
        return mutated_individual

    def _generate_offspring(self, population: list[T], generation: int) -> list[T]:
        sample_size = int(len(population) * self.crossover_rate)
        sample = np.random.choice(population, size=sample_size)
        offsprings = list()

        for _ in range(sample_size):
            individual, partner = np.random.choice(sample, size=2)
            offspring_1, offspring_2 = individual.cross_over(partner, offspring_gen=generation)
            offsprings.append(offspring_1)
            offsprings.append(offspring_2)

        return offsprings

    def _apply_tragedy(self, population: list[T]) -> list[T]:
        surviving_rate = 1 - self.tragedy_rate
        survivor_sample_size = int(len(population) * surviving_rate)
        survivors = np.random.choice(population, size=survivor_sample_size)
        return list(survivors)

    def select_top_n_from(self, population: list[T], n: int) -> list[T]:
        selected = sorted(population, key=lambda individual: individual.score)
        return selected[0:n]

    def generate_individuals_until(self, gen: int) -> list[T]:
        population = self.initial_population

        for gen in track(range(1, gen + 1), description=f"Processing {gen} Generations..."):
            if gen % self.tragedy_on_every_nth_generation == 0:
                population = self._apply_tragedy(population=population)
            else:
                mutons = self._generate_mutons(population=population, generation=gen)
                offsprings = self._generate_offspring(population=population, generation=gen)
                population = self.select_top_n_from(
                    population=population + mutons + offsprings, n=self.top_n
                )

        return population
