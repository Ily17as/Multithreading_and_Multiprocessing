import os


def check_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    script_dir = os.path.dirname(__file__)
    # .. означает "подняться" на один уровень вверх
    parent_dir = os.path.join(script_dir, "..")
    filepath = os.path.join(parent_dir, "primes_nonoptimized.txt")

    with open(filepath, "w") as file:
        for i in range(1, 1000001):
            if check_prime(i):
                file.write(str(i) + "\n")


if __name__ == "__main__":
    main()
