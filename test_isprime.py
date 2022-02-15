def is_prime(n):
    if type(n) != int:
        raise TypeError
    if n <= 1:
        raise ValueError
    for divisor in range(2, int(n ** 0.5) + 2):
        if n % divisor == 0:
            return False
    return True

if __name__ == "__main__":

    try:
        n = int(input())
        ans = is_prime(n)
    except ValueError:
        print('NO')
    else:
        print("YES") if ans else "NO"
