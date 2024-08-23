def is_prime(func):
    def wrapper(*args):
        func_result = func(*args)
        if func_result <= 1:
            return f'Число {func_result} не является простым/составным'
        elif all(func_result % i != 0 for i in range(2, int(func_result ** 0.5) + 1)):
            return f'Число {func_result} является простым'
        else:
            return f'Число {func_result} является составным'

    return wrapper


@is_prime
def sum_three(*args):
    summary = sum(args)
    return summary


result = sum_three(2, 3, 6)
print(result)
