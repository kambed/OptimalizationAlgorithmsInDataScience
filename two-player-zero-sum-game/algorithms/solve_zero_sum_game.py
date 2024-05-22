import logging
import math

from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, lpSum


def solve_zero_sum_game(matrix):
    scaled_matrix, scale_value = _upscale_matrix_if_contains_negative_values(matrix)

    a_problem_primary_variables = _solve_lp_problem(scaled_matrix, LpMinimize)
    logging.debug(f"Primary variables for player A: {a_problem_primary_variables}")
    b_problem_primary_variables = _solve_lp_problem(scaled_matrix, LpMaximize)
    logging.debug(f"Primary variables for player B: {b_problem_primary_variables}")

    game_value = 1 / math.fsum(a_problem_primary_variables)
    player_a = [round(var * game_value, 2) for var in a_problem_primary_variables]
    player_b = [round(var * game_value, 2) for var in b_problem_primary_variables]
    final_game_value = round(game_value - scale_value, 2)

    return final_game_value, player_a, player_b


def _upscale_matrix_if_contains_negative_values(matrix):
    min_value_in_matrix = float(matrix.min())
    scale_value = 0
    if min_value_in_matrix <= 0:
        scale_value = abs(min_value_in_matrix)
        matrix = matrix + scale_value
    return matrix, scale_value


def _solve_lp_problem(matrix, sense):
    problem = LpProblem("LP_Problem", sense)
    row, col = matrix.shape
    if sense == LpMaximize:
        col, row  = matrix.shape
    variables = [LpVariable(f"x{i + 1}", 0) for i in range(row)]
    problem += lpSum(variables)

    for j in range(col):
        if sense == LpMinimize:
            problem += lpSum(variables[i] * matrix[i, j] for i in range(row)) >= 1
        elif sense == LpMaximize:
            problem += lpSum(variables[i] * matrix[j, i] for i in range(row)) <= 1

    problem.solve()
    return [var.value() for var in variables]
