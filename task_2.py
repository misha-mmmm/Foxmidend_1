# import time
# import functools
# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(run_time)
#         return result
#     return wrapper
#
#
# @timer
# def slow_sum(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
# print(slow_sum(5))
# LEVEL 4
# import functools
# import time
#
# def count_calls(func):
#     calls = 0
#     @functools.wraps(func)
#     def wrapper(a, b):
#         nonlocal calls
#         calls += 1
#         print("call:", calls)
#         return func(a, b)
#     return wrapper
#
# def timer(func):
#     @functools.wraps(func)
#     def wrapper(a, b):
#         start = time.time()
#         result = func(a, b)
#         end = time.time()
#         print("time:", end - start)
#         return result
#     return wrapper
#
# @timer
# @count_calls
#
# def multiply(a, b):
#     return a * b
#
# print(multiply(2, 3))
# print(multiply(4, 5))
# print(multiply(6, 7))
# LEVEL 5
# from functools import cache
#
# def count_calls(func):
#     def wrapper(n):
#         wrapper.calls += 1
#         print("call:", wrapper.calls)
#         return func(n)
#     wrapper.calls = 0
#     return wrapper
#
# @count_calls
# @cache
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(10))
#LEVEL 6
# import time
#
# def slow_down(func):
#     def wrapper(n):
#         time.sleep(1)
#         return func(n)
#     return wrapper
#
# @slow_down
# def countdown(n):
#     if n < 0:
#         return
#     print(n)
#     countdown(n - 1)
#
# countdown(3)
#LEVEL 7
# import time
#
# def slow_down(seconds):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(seconds)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#     print("slow:", seconds)
#     print("fast:", seconds)
#
# @slow_down(0.5)
# def countdown_fast(n):
#     if n < 0:
#         return
#     print("fast:", n)
#     countdown_fast(n - 1)
#
# @slow_down(2)
# def countdown_slow(n):
#     if n < 0:
#         return
#     print("slow:", n)
#     countdown_slow(n - 1)
#
# countdown_fast(3)
# print("------")
# countdown_slow(3)
#LEVEL 8
# def repeat(times):
#     def decorator(func):
#         def wrapper():
#             for _ in range(times):
#                 func()
#         return wrapper
#     return decorator
#
# @repeat(times=4)
# def say_hello():
#     print("Hello!")
#
# say_hello()
#LEVEL 9
# def retry(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             try:
#                 x = int(input("Введи число: "))
#                 print(10 / x)
#             except retry(ValueError):
#                 print("На нуль ділити не можна")
#             for i in range(times):
#                 func()
#         return wrapper
#     return decorator
#
#
# @retry(times=3)
# def unstable_function(): ...
# unstable_function()



