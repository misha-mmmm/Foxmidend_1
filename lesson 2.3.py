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


if __name__ == "__main__":
    tekst()
