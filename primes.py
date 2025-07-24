# primes.py

def is_prime(num):
    """
    Returns True if num is a prime number, else False.
    """
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def primes_up_to(num):
    """
    Returns a list of prime numbers between 2 and num inclusive.
    """
    primes = []
    for i in range(2, num + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def main():
    while True:
        try:
            limit = int(input("Enter the number up to which you want to find primes: "))
            if limit < 2:
                print("Please enter a number greater than or equal to 2.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    primes_list = primes_up_to(limit)
    print(f"Primes up to {limit}: {primes_list}")

    see_count = input("Do you want to see how many primes were found? (yes/no): ").strip().lower()
    if see_count in ['yes', 'y']:
        print(f"Number of primes found: {len(primes_list)}")
    else:
        print("Okay, no problem!")

if __name__ == "__main__":
    main()