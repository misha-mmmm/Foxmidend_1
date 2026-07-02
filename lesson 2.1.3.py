# import time
#
# def delay(func):
#     def wrapper():
#         time.sleep(1)
#         func()
#     return wrapper
#
#
# @delay
# def tekst():
#     print("dfhisgfihashdiasbdhi")
#
#
# tekst()
#



import time

def delay(seconds):
    def decorator(func):
        def wrapper():
            time.sleep(seconds)
            func()
        return wrapper
    return decorator


@delay(2)
def tekst():
    print("dajdhajihdhxabdkhagdwh")


tekst()