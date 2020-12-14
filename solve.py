from pysat.formula import CNF
from pysat.solvers import Solver


def solve(formula: CNF):
    """Solves a CNF using a m22 SAT-solver

    :param formula: The CNF to solve
    :return: A tuple containing the formula's satisfiability and its solution, if any
    """
    solver = Solver(bootstrap_with=formula.clauses)

    is_solvable = solver.solve()

    if is_solvable:
        result = (True, solver.get_model())
    else:
        result = (False, None)

    solver.delete()

    return result


def rep_sol(sol: (bool, [int]), size: int):
    """Displays a solution textually

    :param sol: The solution tuple as generated by the `solve` method
    :param size: The number of rows/cols in the board to display
    """
    if not sol[0]:
        print("NO SOLUTION")
        return

    for r in range(size):
        truths = [" X " if i+(r*size)+1 in sol[1] else "   " for i in range(size)]
        print("|".join(truths))


