import math

from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, PULP_CBC_CMD, lpSum

"""
    Solves a zero-sum game using linear programming.

    Args:
        matrix (np.ndarray): Payoff matrix of the game.

    Returns:
        Tuple[List[float], List[float], float]: Mixed strategies for player A, mixed strategies for player B, and the value of the game.
    """
def solve_zero_sum_game(matrix):
    scaled_matrix, scale_value = _scale_matrix(matrix)
    rows_number, cols_number = scaled_matrix.shape

    a_problem_variables = _solve_lp_problem(scaled_matrix, rows_number, cols_number, LpMinimize, minimize=True)
    b_problem_variables = _solve_lp_problem(scaled_matrix, rows_number, cols_number, LpMaximize, minimize=False)

    game_value = 1 / math.fsum(a_problem_variables)
    player_a = [round(var * game_value, 2) for var in a_problem_variables]
    player_b = [round(var * game_value, 2) for var in b_problem_variables]
    final_game_value = round(_calculate_game_value(game_value, scale_value), 2)

    return final_game_value, player_a, player_b


"""
    Scales the matrix to ensure all values are positive.

    Args:
        matrix (np.ndarray): The original payoff matrix.

    Returns:
        Tuple[np.ndarray, float]: The scaled matrix and the scaling value.
    """
def _scale_matrix(matrix):
    min_value_in_matrix = float(matrix.min())
    if min_value_in_matrix <= 0:
        matrix = matrix + abs(min_value_in_matrix)
    return matrix, min_value_in_matrix


"""
    Solves the linear programming problem for the game.

    Args:
        matrix (np.ndarray): The scaled payoff matrix.
        rows_number (int): Number of rows in the matrix.
        cols_number (int): Number of columns in the matrix.
        sense: The sense of the LP problem (LpMinimize or LpMaximize).
        minimize (bool): True if minimizing (for player A), False if maximizing (for player B).

    Returns:
        List[float]: The solution variables from the LP problem.
    """
def _solve_lp_problem(matrix, rows_number, cols_number, sense, minimize):
    problem = LpProblem("LP_Problem", sense)
    if minimize:
        variables = [LpVariable(f"X{i + 1}", 0) for i in range(rows_number)]
        problem += lpSum(variables)

        for j in range(cols_number):
            problem += lpSum(variables[i] * matrix[i, j] for i in range(rows_number)) >= 1

    else:
        variables = [LpVariable(f"Y{j + 1}", 0) for j in range(cols_number)]
        problem += lpSum(variables)

        for i in range(rows_number):
            problem += lpSum(variables[j] * matrix[i, j] for j in range(cols_number)) <= 1

    problem.solve(PULP_CBC_CMD(msg=False))
    return [var.varValue for var in variables]


"""
    Calculates the final game value considering the scaling.

    Args:
        game_value (float): The game value from the LP solution.
        scale_value (float): The value used to scale the matrix.

    Returns:
        float: The final game value.
    """
def _calculate_game_value(game_value, scale_value):
    return game_value - abs(scale_value) if scale_value <= 0 else game_value
