# import functools
# import time
#
#
# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         print(f"{func.__name__} finished in {end - start:.4f} sec")
#         return result
#     return wrapper
#
#
# def count_calls(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.num_calls += 1
#         return func(*args, **kwargs)
#     wrapper.num_calls = 0
#     return wrapper
#
#
# @timer
# @count_calls
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(20))
# print("Total calls:", fibonacci.num_calls)
#
#

