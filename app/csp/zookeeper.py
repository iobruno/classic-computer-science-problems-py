from app.csp.constraints import Constraint


class ZookeeperConstraint:
    class Rejects(Constraint[str, str]):
        def __init__(self, animal: str, neighbor_animal: str, reason: str = None):
            super().__init__([animal, neighbor_animal])
            self.animal1: str = animal
            self.animal2: str = neighbor_animal
            self.reason: str = reason

        def is_satisfied_with(self, assignment: dict[str, int]) -> bool:
            """
            Rules:
            - If animal2 is not assigned, the cage is available for animal1, and vice versa.
            - If both are assigned, the constraint is only satisfied if they don't share the cage.
            """
            if self.animal1 not in assignment or self.animal2 not in assignment:
                return True

            return assignment[self.animal1] != assignment[self.animal2]

    class RejectsSameOrAdjacent(Constraint[str, str]):
        def __init__(self, animal: str, another_animal: str, reason: str = None):
            super().__init__([animal, another_animal])
            self.animal1 = animal
            self.animal2 = another_animal
            self.reason: str = reason

        def is_satisfied_with(self, assignment: dict[str, int]) -> bool:
            """
            Rules:
            - If animal2 is not assigned, the cage is available for animal1, and vice versa.
            - If both are assigned, the constraint is satisfied only if:
              * they are neither in the same cage,
              * nor in adjacent cages.
            """
            if self.animal1 not in assignment or self.animal2 not in assignment:
                return True

            animal1_cage: int = assignment[self.animal1]
            animal2_cage: int = assignment[self.animal2]
            return abs(animal1_cage - animal2_cage) > 1

    class MustBeTogetherWith(Constraint[str, str]):
        def __init__(self, animal: str, neighbor_animal: str, reason: str = None):
            super().__init__([animal, neighbor_animal])
            self.animal1: str = animal
            self.animal2: str = neighbor_animal
            self.reason: str = reason

        def is_satisfied_with(self, assignment: dict[str, str]) -> bool:
            """
            Represents the configuration of animal assignments to cages.
            Meaning:
            - If animal2 is not assigned, the cage is available for animal1.
            - If both are assigned, the constraint is only satisfied they share the same cage
            """
            if self.animal1 not in assignment or self.animal2 not in assignment:
                return True

            return assignment[self.animal1] == assignment[self.animal2]

    class MustBeInCageID(Constraint[str, int]):
        def __init__(self, animal: str, cage: int, reason: str = None):
            super().__init__([animal])
            self.animal: str = animal
            self.cage_number: int = cage
            self.reason: str = reason

        def is_satisfied_with(self, assignment: dict[str, int]) -> bool:
            """
            Rules:
            - The animal must be assigned to the specified cage for the constraint to be satisfied,
            otherwise, it is rejected.
            """
            return assignment[self.animal] == self.cage_number
