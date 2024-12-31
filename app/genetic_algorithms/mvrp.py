from dataclasses import dataclass
from itertools import tee
from random import sample
from typing import TypeVar

import numpy as np

from app.genetic_algorithms.individual import Chromosome, Individual
from app.genetic_algorithms.utils import delivery_points, dist_between

T = TypeVar("T", bound="MultiVehicleRoutingProblem")
C = TypeVar("C", bound="Vehicle")
G = TypeVar("G")


@dataclass
class Vehicle(Chromosome):
    """
    Each vehicle is represented by a Chromosome in this scenario
    And the set of chromosomes (or Vehicles) defines an Individual
    """

    def __init__(self, initial_route):
        super().__init__(genes=initial_route)
        self.route = self._traceroute()
        self.score = self.fitness()

    def fitness(self):
        overall_distance = [dist_between(start, end) for start, end in self.route]
        return sum(overall_distance)

    def _traceroute(self) -> list[tuple[G, G]]:
        src, dst = tee(self._compute_route())
        next(dst)
        return list(zip(src, dst))

    def _compute_route(self) -> np.ndarray:
        genes = np.insert(self.genes, 0, 0, axis=0)
        genes = np.append(genes, 0)
        return genes


@dataclass
class MultiVehicleRoutingProblem(Individual):
    """
    Each individual is a representation of a possible solution to the problem
    we're trying to solve.

    It should contain a set of one or more chromosomes, so long as each
    chromosome solves part of the problem
    """

    def __init__(self, vehicles, gen=1):
        super().__init__(chromosomes=vehicles, gen=gen)
        self.score = self.fitness()
        self.no_chromosomes = len(vehicles)

    @property
    def vehicles(self) -> list[C]:
        return self.chromosomes

    def fitness(self) -> int:
        individual_fitness_results = [vehicle.fitness() for vehicle in self.vehicles]
        return sum(individual_fitness_results)

    def mutate(self, gen: int) -> T:
        slices: int = self.no_chromosomes
        flattened_genes = self.flatten_genes()
        np.random.shuffle(flattened_genes)
        vehicle_routes: list[np.ndarray] = np.array_split(flattened_genes, slices)
        vehicles = [Vehicle(initial_route=route) for route in vehicle_routes]
        return MultiVehicleRoutingProblem(vehicles=vehicles, gen=gen)

    def cross_over(self, other: T, offspring_gen: int) -> tuple[T, T]:
        """
        Davis’ Order Crossover (OX1)
        - Create two random crossover points in the parent,
          and copy the segment between them from the first parent to the first offspring.

        - Starting from the second crossover point in the second parent,
          copy the remaining unused numbers from the second parent to the first child,
          wrapping around the list.
        """
        first_parent_genes = self.flatten_genes()
        second_parent_genes = other.flatten_genes()

        first_offspring = self._make_offspring_from(
            first_parent=first_parent_genes,
            second_parent=second_parent_genes,
        )
        second_offspring = self._make_offspring_from(
            first_parent=second_parent_genes,
            second_parent=first_parent_genes,
        )

        first_individual = MultiVehicleRoutingProblem.generate_from(
            all_delivery_points=first_offspring,
            gen=offspring_gen,
            with_split=self.no_chromosomes,
        )

        second_individual = MultiVehicleRoutingProblem.generate_from(
            all_delivery_points=second_offspring,
            gen=offspring_gen,
            with_split=self.no_chromosomes,
        )
        return first_individual, second_individual

    def _make_offspring_from(
        self, first_parent: np.ndarray, second_parent: np.ndarray
    ) -> np.ndarray:
        # Cross Over Points (A, B)
        a, b = sample(range(1, len(first_parent)), 2)
        if a > b:
            a, b = b, a

        cross_over_points = [a, b]
        offspring = np.zeros(len(first_parent), dtype=int)
        o1, o2, o3 = np.split(offspring, cross_over_points)

        # Copying the segment between the cross_over points
        # from the first parent to the first offspring
        for idx in range(len(o2)):
            o2[idx] = first_parent[idx]

        # Fills up first and third segments
        included_nodes = set(o2)
        target = o1
        idx = 0

        for elem in second_parent:
            if elem not in included_nodes:
                if idx < len(target):
                    target[idx] = elem
                else:
                    target = o3
                    idx = 0
                    o3[idx] = elem
                idx += 1
                included_nodes.add(elem)

        return np.concatenate([o1, o2, o3])

    @classmethod
    def generate_from(cls, all_delivery_points: np.ndarray, gen: int, with_split) -> T:
        return cls._split_cargo(all_delivery_points, gen, with_split)

    @classmethod
    def generate_random(cls, gen: int, with_split) -> T:
        all_delivery_points = np.copy(delivery_points)
        np.random.shuffle(all_delivery_points)
        return cls._split_cargo(all_delivery_points, gen, with_split)

    @classmethod
    def _split_cargo(cls, all_delivery_points: np.ndarray, gen: int, with_split) -> T:
        vehicle_routes = np.array_split(all_delivery_points, with_split)
        vehicles = [Vehicle(initial_route=route) for route in vehicle_routes]
        individual: MultiVehicleRoutingProblem = cls(vehicles=vehicles, gen=gen)
        return individual
