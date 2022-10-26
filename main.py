from datetime import datetime
import logging
from multiprocessing import Pool, cpu_count


def factorize_num(n):
    i = 1
    a = []
    while i ** 2 <= n:
        if n % i == 0:
            a.append(i)
            if i != n // i:
                a.append(n // i)
        i += 1

    a.sort()
    return a


def factorize(*number):

    result = []
    start_time = datetime.now()
    # for n in number:
    #     result.append(factorize_num(n))
    with Pool(cpu_count()) as p:
        result = p.map(factorize_num, [n for n in number])

    logging.debug(f"Working time : {datetime.now() - start_time}")
    return result


def main():
    logging.basicConfig(level=logging.DEBUG)

    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
                 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


if __name__ == "__main__":
    main()
