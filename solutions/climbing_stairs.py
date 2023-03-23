"""Solves puzzle to calculate the number of ways you can climb up a stairs"""


def permutation_calculator(n_steps: int, max_step_size: int) -> int:
    """
    Calculates the number of ways you can walk up a stairs with n_steps,
    when you can take max_step_size steps at a time
    """
    max_step_size = min(n_steps, max_step_size)
    if n_steps == 0:
        return 1

    return sum(
        map(
            lambda x: permutation_calculator(n_steps - x, max_step_size),
            range(1, max_step_size + 1),
        )
    )


def faster_permutation_calculator(n_steps: int, max_step_size: int) -> int:
    """
    A faster way to calculate the number of ways you can walk up a stairs with n_steps,
    when you can take max_step_size steps at a time.
    """
    max_step_size = min(n_steps, max_step_size)
    if n_steps < 0 or max_step_size < 1:
        raise ValueError('No solution')

    if n_steps < 1 or max_step_size == 1:
        return 1

    solution_per_step = [1, 1]  # solution for steps 0 and 1
    for i in range(2, n_steps + 1):
        if max_step_size >= i:
            current_step = sum(solution_per_step)
        else:
            current_step = 0
            for j in range(1, max_step_size + 1):
                current_step += solution_per_step[-j]

        solution_per_step.append(current_step)

    return solution_per_step[-1]
