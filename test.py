from datetime import datetime
from time import sleep
from os import cpu_count
from multiprocessing import Pool


# def factorize(*number_list):
#     result = []
#     for numbers in number_list:
#         one_result = []
#         for num in range(1, numbers + 1):
#             if numbers % num == 0:
#                 one_result.append(num)
#         result.append(one_result)
#     return result
#
#
# now = datetime.now()
# a, b, c, d = factorize(128, 255, 99999, 10651060)
# sleep(1)
# print(datetime.now() - now)
#
# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530,
#              10651060]


def factorize(number):
    one_result = []
    for num in range(1, number + 1):
        if number % num == 0:
            one_result.append(num)
    return one_result


start = datetime.now()
with Pool(processes=cpu_count()) as pool:
    a, b, c, d = pool.map(factorize, [128, 255, 99999, 10651060])
sleep(1)
print(datetime.now() - start)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530,
             10651060]
