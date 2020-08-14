import pycosat
from item import Item


class SATSolver:

    @staticmethod
    def get_solutions(number, cnf):
        solutions = []
        i = 0
        for sol in pycosat.itersolve(cnf):
            if i == number:
                break
            i += 1
            solutions.append(sol)
        print("Successfully generated", i, "solutions")
        binary_solutions = [[1 if val > 0 else 0 for val in sol] for sol in solutions]
        items = [Item(item) for item in binary_solutions]
        return items
