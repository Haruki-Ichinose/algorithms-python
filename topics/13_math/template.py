from math import gcd


def divisors(n):
    result = []
    for x in range(1, int(n**0.5) + 1):
        if n % x == 0:
            result.append(x)
            if x * x != n:
                result.append(n // x)
    return sorted(result)


def main():
    print(gcd(12, 18))
    print(divisors(36))


if __name__ == "__main__":
    main()
