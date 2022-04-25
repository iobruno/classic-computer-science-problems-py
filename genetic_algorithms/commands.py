import click
from genetic_algorithms.individual import Individual
from genetic_algorithms.algorithm import GeneticAlgorithm
from typing import List
from genetic_algorithms.mvrp import MultiVehicleRoutingProblem as mvrp
from rich.progress import Console, track

console = Console()


@click.group()
def ga():
    pass


@ga.command("mvrp")
def multi_vehicle_roting_problem():
    console.print("Generating Initial batch with 10K individuals...")
    initial_batch = generate_initial_batch_of(10000, split_between=4)
    algorithm = GeneticAlgorithm(initial_population=initial_batch,
                                 mutation_rate=0.5,
                                 crossover_rate=0.3,
                                 tragedy_rate=0.15,
                                 tragedy_on_every_nth_generation=1000)

    console.print("Cycling through generations, this may take a while...")
    individuals: List[Individual] = algorithm.generate_individuals_until(generation=5000)

    console.print("All done, preparing to print top N individuals...")
    fmt_print(individuals, n=100)


def generate_initial_batch_of(n: int, split_between: int):
    return [mvrp.generate_random(gen=0, with_split=split_between)
            for _ in track(range(n), description=f"Initial batch of {n}")]


def fmt_print(individuals: List[Individual], n: int):
    console.print(f"Now listing the Top {n} Best Individuals")
    for indv in individuals[0:n]:
        console.print(indv)


if __name__ == "__main__":
    multi_vehicle_roting_problem()