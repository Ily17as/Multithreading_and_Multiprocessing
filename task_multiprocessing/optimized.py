from multiprocessing import Pool


def check_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    filepath = "primes_optimized.txt"

    with Pool() as pool:
        numbers = list(range(1, 1000001))
        results = pool.map(check_prime, numbers)

    primes = [str(num) for num, is_prime in zip(numbers, results) if is_prime]

    with open(filepath, "w") as f:
        f.write("\n".join(primes))  # 123


if __name__ == "__main__":
    main()
