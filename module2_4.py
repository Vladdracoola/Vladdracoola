numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    elif i < 4: # Подскажите, пожалуйста, можно ли было сделать это универсальнее?
        primes.append(i)
    elif i % 2 == 0 or i % 3 == 0: # Так как 2 и 3 здесь буду исключениями...
        not_primes.append(i)
    else:
        primes.append(i)

print('Primes ',primes)
print('Not primes ', not_primes)