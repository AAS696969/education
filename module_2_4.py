numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    is_prime = True
    n = numbers[i]
    if n < 2:
        continue
    else:
        k = 0
        for y in range(2, n // 2 + 1):
            if n % y == 0:
                k = k + 1
        if (k <= 0):
            primes.append(n)
        else:
            not_primes.append(n)
print('Простые числа ', primes)
print('Составные числа', not_primes)