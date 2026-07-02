# # #common decorator's structure
# #
# # import functools
# #
# #
# # def decorator(func):
# #     @functools.wraps(func)
# #     def wrapper(*args, **kwargs):
# #         # To do before...
# #         value = func(*args, **kwargs)
# #         # To do after...
# #         return value
# #     return wrapper
# from os import times_result
#
#
#
# import functools
# import time
#
# import timer
#
#
#
# def timer(func):
#     """Print the time taken to execute the function"""
#
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Finished {func.__name__} () in {run_time:.4f} seconds)")
#         return value
#
#     return wrapper_timer
#
# # @timer
# # def some_haavy_function(num: int) -> int:
# #     return sum((num ** 2 for _ in range(10_000_000)))
# #
# # print(some_haavy_function(150))
#
#
#
# @timer
# def fibonacci(num: int) -> int:
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
#
# print(fibonacci(30))
#
#
# import functools
# import time
# def timer(func):
#     """Print the runtime of thw decorated function"""
#
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Finished {func.__name__} () in {run_time:.4f} seconds")
#         return value
#     return wrapper_timer
#
# def count_calls(func):
#     @functools.wraps(func)
#     def wrapper_count_calls(*args, **kwargs):
#         wrapper_count_calls.num_calls += 1
#         print(f"Call  {wrapper_count_calls.num_calls} of {func.__name__}()")
#         return func(*args, **kwargs)
#
#     wrapper_count_calls.num_calls = 0
#     return wrapper_count_calls
#
#
#
# @timer
# @count_calls
# def fibonacci(num: int) -> int:
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
#
#
# print(fibonacci(30))
#
#
# import functools
# import time
#
#
# def cache(func):
#     """Keep a cache of previous function calls"""
#     @functools.wraps(func)
#     def wrapper_cache(*args, **kwargs):
#         cache_key = args + tuple(kwargs.items())
#         if cache_key not in wrapper_cache.cache:
#             wrapper_cache.num_func_calls += 1
#             wrapper_cache.cache[cache_key] = func(*args, **kwargs)
#             print(f"Call {wrapper_cache.num_func_calls} of {func.__name__}()")
#         else:
#             wrapper_cache.num_cache_returns += 1
#             print(f"Returned {wrapper_cache.num_cache_returns} times from cashe")
#         return wrapper_cache.cache[cache_key]
#     wrapper_cache.cache = {}
#     wrapper_cache.num_func_calls = 0
#     wrapper_cache.num_cache_returns = 0
#     return wrapper_cache
#
#
# def time(func):
#     """Print the time taken to execute the function"""
#
#     @functools.wraps(func)
#     def wrapper_time(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Finished {func.__name__} () in {run_time:.4f} seconds")
#         return value
#
#     return wrapper_time
#
#
# @timer
# @cache
# def fibonacci(num: int) -> int:
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
#
#
# print(fibonacci(30))
#
# import functools
#
#
#
# def timer(func):
#     """Print the runtime of thw decorated function"""
#
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Finished {func.__name__} () in {run_time:.4f} seconds")
#         return value
#     return wrapper_timer
#
#
# @timer
# @functools.lru_cache(maxsize=30)
# def fibonacci(num: int) -> int:
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)
#
#
#
# print(fibonacci(30))
#
