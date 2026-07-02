# TASK 1
# LEVEL 1
# def log_call(func):
#     def wrapper():
#         print(f"func {func.__name__} start")
#         func()
#         print(f"func {func.__name__} end")
#     return wrapper
#
# @log_call
# def vitannia():
#     print('hello world')
#
# vitannia()
#
# import time
# from curses import wrapper
# from turtledemo.penrose import start


# LEVEL 2
# def double_result(func):
#     def wrapper():
#         return func() * 2
#     return wrapper
#
# @double_result
# def get_number():
#     return 40
#
# print(get_number())  # 20
#

# LEVEL 3
# def greeting_decorator(func):
#     def wrapper():
#         print("start")
#         func()
#         print("end")
#     return wrapper
#
#
# @greeting_decorator
# def say_something():
#     print("sjhdjdhsjd")


# say_something()

# LEVEL 4
# def print_args(func):
#     def wrapper(*args, **kwargs):
#         print("num:", *args)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @print_args
# def add(a, b):
#     return a + b
#
#
# result = add(2, 5)
# print("Результат:", result)
#
# LEVEL 5
# def measure_time(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print("Time = ", end - start - 1)
#     return wrapper
#
# @measure_time
# def test():
#     time.sleep(1)
#
# test()

# LEVEL 6
# def limit_calls(func):
#     count = 0
#     def wrapper():
#         nonlocal count
#         if count < 3:
#             count += 1
#             func()
#         else:
#             print("Error")
#     return wrapper
#
#
# @limit_calls
# def main():
#     print("dddedwdwdd")
#
# main()
# main()
# main()
# main()

# LEVEL 7
# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for i in range(n):
#                 func()
#         return wrapper
#     return decorator
#
#
# @repeat(3)
# def hello():
#     print("Hi")
#
# hello()

# LEVEL 8
# def only_ints(func):
#     def wrapper(*args):
#         for arg in args:
#             if type(arg) != int:
#                 print("Type Error")
#         return func(*args)
#     return wrapper
#
# @only_ints
# def add(a, b):
#     return a + b
#
# print(add(1, 2))
# print(add(1, "edsdsdsds"))
#
#



# LEVEL 9

# def cache_result(func):
#     cache = {}
#     def wrapper(*args, **kwargs):
#         if args in cache:
#             print("use cache...")
#             return cache[args]
#         result = func(*args, **kwargs)
#         cache[args] = result
#         return result
#     return wrapper
#
# @cache_result
# def multiply(a, b):
#     print("Counting...just wait")
#     return a * b
#
# print(multiply(1, 2))
# print(multiply(1, 2))






# TASK 2
# LEVEL 1
#
# import functools
# import time
#
# calls = 0
#
# def count_calls(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         global calls
#         calls += 1
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print("Час:", end - start)
#         return result
#     return wrapper
#
#
# @timer
# @count_calls
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print("Результат:", fibonacci(20))
# print("Кількість викликів:", calls)
#



# LEVEL 2
# import functools
# import time
#
# calls = 0
#
# def count_calls(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         global calls
#         calls += 1
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print("Час:", end - start)
#         return result
#     return wrapper
#
# def cache(func):
#     @functools.wraps(func)
#     def wrapper(*args):
#         if args not in wrapper.cache:
#             wrapper.cache[args] = func(*args)
#         return wrapper.cache[args]
#     wrapper.cache = {}
#     return wrapper
#
#
# @cache
# @timer
# @count_calls
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print("Результат:", fibonacci(20))
# print("Результат:", fibonacci(20))
# print("Кількість викликів:", calls)
#
# LEVEL 3
# import time
#
#
# def count_calls(func):
#     def wrapper(*args, **kwargs):
#         print("count_calls: fync call")
#         return func(*args, **kwargs)
#     return wrapper
#
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print("timer: use time =", end - start)
#         return result
#     return wrapper
#
#
# # V1
# @timer
# @count_calls
# def square1(n):
#     return n * n
#
#
# # V2
# @count_calls
# @timer
# def square2(n):
#     return n * n
#
#
# print("V 1:")
# print(square1(5))
#
# print("V 2:")
# print(square2(5))

# LEVEL 4
# import time
# import functools
#
#
# def delay_one_second(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         time.sleep(1)
#         return func(*args, **kwargs)
#     return wrapper
#
# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} took {end - start} seconds")
#         return result
#     return wrapper
#
# @delay_one_second
# @timer
# def get_data():
#     return "data"
#
# print("data:")
# print(get_data())
