from multiprocessing import Pool
from time import time

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def multi_factorize(*numbers):
    with Pool(processes=len(numbers)) as pool:
        return pool.map(factorize, numbers)

if __name__ == '__main__':
    args_val = [128, 255, 99999, 10651060, 106510607, 1065106078, 1065106079]
    start_time1 = time()
    print("Synchronous code")

    for i in args_val:
        #factorize(i)
        print(f"for number {i} factors: {factorize(i)}")
        

    end_time1 = time()
    execution_time1 = end_time1 - start_time1
    print(f"Execution time: {execution_time1} seconds \n")

    print("Asynchronous code")
    start_time2 = time()

    a, b, c, d, e, f, g = multi_factorize(*args_val)
    #a, b, c = multi_factorize(*args_val)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    print(f"factors: {a}")
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    print(f"factors: {b}")
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    print(f"factors: {c}")
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print(f"factors: {d}")
    assert e == [1, 7, 1061, 7427, 14341, 100387, 15215801, 106510607]
    print(f"factors: {e}")
    assert f == [1, 2, 1303, 2606, 408713, 817426, 532553039, 1065106078]
    print(f"factors: {f}")
    assert g == [1, 263, 4049833, 1065106079]
    print(f"factors: {g}")

    end_time2 = time()
    execution_time = end_time2 - start_time2
    print(f"Execution time: {execution_time} seconds")


# Synchronous code
# for number 128 factors: [1, 2, 4, 8, 16, 32, 64, 128]
# for number 255 factors: [1, 3, 5, 15, 17, 51, 85, 255]
# for number 99999 factors: [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# for number 10651060 factors: [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
# for number 106510607 factors: [1, 7, 1061, 7427, 14341, 100387, 15215801, 106510607]
# for number 1065106078 factors: [1, 2, 1303, 2606, 408713, 817426, 532553039, 1065106078]
# for number 1065106079 factors: [1, 263, 4049833, 1065106079]
# Execution time: 107.7033224105835 seconds

# Asynchronous code
# factors: [1, 2, 4, 8, 16, 32, 64, 128]
# factors: [1, 3, 5, 15, 17, 51, 85, 255]
# factors: [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# factors: [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
# factors: [1, 7, 1061, 7427, 14341, 100387, 15215801, 106510607]
# factors: [1, 2, 1303, 2606, 408713, 817426, 532553039, 1065106078]
# factors: [1, 263, 4049833, 1065106079]
# Execution time: 51.804147481918335 seconds
   