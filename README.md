# Prime Numbers Finder - Interactive Version (MINI Proyect)

This Python script lets you find all prime numbers up to a number you specify interactively.

## Features

- Asks the user to enter the upper limit number to find primes up to.
- Prints the list of prime numbers from 2 up to the number entered.
- Asks if the user wants to see how many primes were found, and shows the count if requested.

## Usage

Run the script:

```bash
python primes.py
```

The program will:

1. Prompt you to enter the upper limit number.
2. Display all prime numbers up to that number.
3. Ask if you want to see the count of prime numbers found.

Example interaction:

```
Enter the number up to which you want to find primes: 20
Primes up to 20: [2, 3, 5, 7, 11, 13, 17, 19]
Do you want to see how many primes were found? (yes/no): yes
Number of primes found: 8
```

## How it works

The program uses a function `is_prime(num)` to check if a number is prime by testing divisibility from 2 up to the number -1.

The `primes_up_to(num)` function creates a list of all prime numbers up to the entered number.

The main function handles user input and displays results accordingly.

## License

This project is licensed under the MIT License.
