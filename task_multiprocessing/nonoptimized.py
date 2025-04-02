def check_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    filepath = "primes_nonoptimized.txt"
    with open(filepath, "w") as file:
        for i in range(1, 1000001):
            if check_prime(i):
                file.write(str(i) + "\n")
            if i == 999983:
                file.write(str(i))


if __name__ == "__main__":
    main()
