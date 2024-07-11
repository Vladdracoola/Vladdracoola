numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    help_count = 0
    if i == 1:
        continue
    for j in range(2,i):
        result = i % j
        if result == 0:
            help_count += 1
            break
    if help_count == 0:
        primes.append(i)
    else: not_primes.append(i)
print('Primes: ', primes)
print("Not primes: ", not_primes)
