def reverse_sequence(n):
    solution = []
    subtractor = 1
    for i in range(n):
        if i == 0:
            solution.append(n)
        else:
            solution.append(n - subtractor)
            subtractor += 1
    return solution
