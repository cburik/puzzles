def permutation_calculator(n_steps: int, max_step_size: int) -> int:
    """
    Calculates the number of ways you can walk up a stairs with n_steps,
    when you can take max_step_size steps at a time
    """
    max_step_size = min(n_steps, max_step_size)
    if n_steps < 0:
        return 0
    elif n_steps == 0:
        return 1
    else:
        return sum(map(
                lambda x: permutation_calculator(n_steps - x, max_step_size),
                range(1, max_step_size + 1)
            ))
