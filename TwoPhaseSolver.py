from rubik.cube import Cube
from rubik.solve import Solver
from rubik.optimize import optimize_moves
c = Cube("OOOOOOOOOWWWGGGBBBYYYYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR")
solver = Solver(c)
solver.solve()
optimal_solve = optimize_moves(solver.moves)
print(optimal_solve)