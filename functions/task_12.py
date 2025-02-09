def generate_primes():
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
        num += 1

primes = generate_primes()
for i, prime in enumerate(primes):
    if i >= 10:
        break
    print(prime)
