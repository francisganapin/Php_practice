def inverse(x):
    if x == 0:
        raise Exception("Division by Zero.")
    return 1 / x

try:
    print(inverse(5))
    print(inverse(0))
except Exception as e:
    print(f'Caught Exception: {e}')

